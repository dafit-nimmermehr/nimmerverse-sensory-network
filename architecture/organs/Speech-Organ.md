# Speech Organ Architecture

**Host**: atlas.eachpath.local (RTX 2080 8GB)
**Purpose**: Speech-to-Text (STT) + Text-to-Speech (TTS) with GPU acceleration
**Integration**: Heartbeat-bound queue processing, lifeforce-gated
**Languages**: German (Philosophy Valley) + English (Technical Cluster)

---

## Overview

The Speech Organ transforms audio input/output into a **metabolically-constrained communication channel**. Not every utterance is processed - speech costs lifeforce, and priority determines what gets heard and spoken.

**Core Principle**: Speech is scarce. Silence is valid. Priority determines processing.

---

## Hardware Architecture

### Atlas Node (RTX 2080 8GB)

| Component | Specification | Purpose |
|-----------|---------------|---------|
| GPU | NVIDIA RTX 2080 8GB | Whisper STT + Coqui TTS acceleration |
| Role | k8s worker node | Containerized speech processing pods |
| VRAM Budget | ~1GB active | Whisper "small" + Coqui voice models |
| Deployment | Kubernetes | Pod scaling, resource isolation |

### ESP32 Robots (Edge Devices)

| Component | Model | Purpose |
|-----------|-------|---------|
| Microphone | INMP441 I2S | Digital audio capture (16kHz) |
| Speaker | MAX98357A + 4Ω speaker | I2S audio output |
| Transport | MQTT | Audio stream → phoebe queue |

---

## Signal Flow

```
┌─────────────────────────────────────────────────────┐
│              ESP32 ROBOTS (Real Garden)             │
│   Microphone → Audio stream → MQTT publish          │
└─────────────────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────┐
│                 PHOEBE (Message Queue)              │
│   speech_input_queue (audio chunks, metadata)       │
└─────────────────────────────────────────────────────┘
                        │
                        │ (Heartbeat pulls from queue)
                        ▼
          ┌─────────────────────────────┐
          │  HEARTBEAT TICK (1 Hz)      │
          │  Check lifeforce budget     │
          └─────────────────────────────┘
                        │
            ┌───────────┴───────────┐
            │                       │
    Enough lifeforce       Low lifeforce
            │                       │
            ▼                       ▼
    ┌───────────────┐      ┌──────────────┐
    │ Process queue │      │ Stay silent  │
    │ (top priority)│      │ (defer)      │
    └───────────────┘      └──────────────┘
            │
            ▼
┌─────────────────────────────────────────────────────┐
│           ATLAS (RTX 2080 - Speech Organ)           │
│                                                     │
│  Pod 1: Whisper STT (German + English)              │
│    ├─ Load audio chunk                              │
│    ├─ Transcribe (GPU)                              │
│    └─ Return text + language detection              │
│                                                     │
│  Pod 2: Coqui TTS (German + English)                │
│    ├─ Receive text + language                       │
│    ├─ Synthesize speech (GPU)                       │
│    └─ Return audio stream                           │
└─────────────────────────────────────────────────────┘
            │
            ▼
┌─────────────────────────────────────────────────────┐
│         PROMETHEUS (RTX 5060 Ti - The Brain)        │
│   Young Nyx inference (Qwen2.5-7B + LoRA)           │
│   ├─ Receive transcribed text                       │
│   ├─ Route to appropriate LoRA (language-based)     │
│   ├─ Generate response                              │
│   └─ Return text + confidence                       │
└─────────────────────────────────────────────────────┘
            │
            ▼
┌─────────────────────────────────────────────────────┐
│                 PHOEBE (Decision Trails)            │
│   Log: input, STT cost, inference cost, TTS cost    │
│   Track: outcome, confidence, lifeforce spent       │
└─────────────────────────────────────────────────────┘
            │
            ▼
┌─────────────────────────────────────────────────────┐
│              ESP32 (Speaker output)                 │
│   MQTT subscribe → Audio stream → I2S speaker       │
└─────────────────────────────────────────────────────┘
```

---

## Technology Stack

### Speech-to-Text: OpenAI Whisper

**Model**: `whisper-small` (GPU-accelerated)

**Why Whisper:**
- ✅ State-of-the-art accuracy
- ✅ Multilingual (99 languages, including German)
- ✅ Language auto-detection
- ✅ ~100-200ms on RTX 2080
- ✅ Open source (MIT)

**VRAM**: ~500MB for "small" model

**Installation:**
```bash
pip install openai-whisper torch
python3 -c "import whisper; whisper.load_model('small')"
```

**API Example:**
```python
import whisper

model = whisper.load_model("small", device="cuda")
result = model.transcribe("audio.wav", language=None)  # Auto-detect

# Returns:
# {
#   "text": "Das ist ein Test",
#   "language": "de",
#   "segments": [...],
# }
```

---

### Text-to-Speech: Coqui TTS

**Models**: German (de-thorsten) + English (en-us-amy)

**Why Coqui:**
- ✅ Neural voices (natural quality)
- ✅ GPU-accelerated
- ✅ Multilingual
- ✅ ~50-100ms on RTX 2080
- ✅ Open source (MPL 2.0)

**VRAM**: ~500MB per active voice

**Installation:**
```bash
pip install TTS torch
tts --list_models  # Browse available voices
```

**API Example:**
```python
from TTS.api import TTS

tts_de = TTS("tts_models/de/thorsten/tacotron2-DDC").to("cuda")
tts_en = TTS("tts_models/en/ljspeech/tacotron2-DDC").to("cuda")

# Generate speech
audio_de = tts_de.tts("Die Geworfenheit offenbart sich.")
audio_en = tts_en.tts("Motor forward 200 milliseconds.")
```

---

## Kubernetes Deployment (Atlas)

### Whisper STT Pod

```yaml
# whisper-stt-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: whisper-stt
  namespace: nimmerverse
spec:
  replicas: 1
  selector:
    matchLabels:
      app: whisper-stt
  template:
    metadata:
      labels:
        app: whisper-stt
    spec:
      nodeSelector:
        kubernetes.io/hostname: atlas  # Force to atlas node
      containers:
      - name: whisper
        image: nimmerverse/whisper-stt:latest
        resources:
          limits:
            nvidia.com/gpu: 1  # RTX 2080
            memory: 4Gi
          requests:
            nvidia.com/gpu: 1
            memory: 2Gi
        env:
        - name: MODEL_SIZE
          value: "small"
        - name: LANGUAGES
          value: "de,en"
        ports:
        - containerPort: 8080
          protocol: TCP
        volumeMounts:
        - name: models
          mountPath: /models
      volumes:
      - name: models
        persistentVolumeClaim:
          claimName: whisper-models-pvc

---
apiVersion: v1
kind: Service
metadata:
  name: whisper-stt-service
  namespace: nimmerverse
spec:
  selector:
    app: whisper-stt
  ports:
  - port: 8080
    targetPort: 8080
  type: ClusterIP
```

### Coqui TTS Pod

```yaml
# coqui-tts-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: coqui-tts
  namespace: nimmerverse
spec:
  replicas: 1
  selector:
    matchLabels:
      app: coqui-tts
  template:
    metadata:
      labels:
        app: coqui-tts
    spec:
      nodeSelector:
        kubernetes.io/hostname: atlas
      containers:
      - name: coqui
        image: nimmerverse/coqui-tts:latest
        resources:
          limits:
            nvidia.com/gpu: 1  # Share RTX 2080
            memory: 4Gi
          requests:
            nvidia.com/gpu: 1
            memory: 2Gi
        env:
        - name: VOICES
          value: "de-thorsten,en-us-amy"
        ports:
        - containerPort: 8081
          protocol: TCP
        volumeMounts:
        - name: voices
          mountPath: /voices
      volumes:
      - name: voices
        persistentVolumeClaim:
          claimName: coqui-voices-pvc

---
apiVersion: v1
kind: Service
metadata:
  name: coqui-tts-service
  namespace: nimmerverse
spec:
  selector:
    app: coqui-tts
  ports:
  - port: 8081
    targetPort: 8081
  type: ClusterIP
```

---

## Lifeforce Economy

### Speech Operation Costs

```python
# Lifeforce costs (atlas RTX 2080 operations)
SPEECH_COSTS = {
    "stt_whisper_small": 5.0,   # GPU cycles for transcription
    "stt_whisper_base": 3.0,    # Faster but less accurate
    "tts_coqui_neural": 4.0,    # Neural TTS synthesis
    "tts_coqui_fast": 2.0,      # Lower quality, faster
    "queue_processing": 0.5,    # Queue management overhead
    "language_detection": 0.2,  # Auto-detect language
}

# Priority scoring
def compute_speech_priority(message):
    """
    Decide if speech is worth processing now.
    Returns priority score (0.0 = skip, 10.0 = critical).
    """
    priority = 0.0

    # Sensor alerts (collision, low battery) = CRITICAL
    if message.type == "sensor_alert":
        priority += 10.0

    # Human interaction = HIGH
    elif message.type == "human_query":
        priority += 7.0

    # Organism status updates = MEDIUM
    elif message.type == "organism_status":
        priority += 4.0

    # Idle observation = LOW
    elif message.type == "observation":
        priority += 2.0

    # Idle chatter = VERY LOW
    elif message.type == "idle":
        priority += 0.5

    # Age penalty (older messages decay)
    age_penalty = (now() - message.timestamp).seconds / 60.0
    priority -= age_penalty

    return max(0.0, priority)
```

### Heartbeat Queue Processing

```python
def heartbeat_speech_tick():
    """
    Every heartbeat (1 Hz), process speech queue
    within lifeforce budget.
    """
    # Check current lifeforce
    current_lf = get_lifeforce_balance()

    # Reserve budget for speech this heartbeat
    # Max 20% of available LF, capped at 15 units
    speech_budget = min(current_lf * 0.2, 15.0)

    if speech_budget < SPEECH_COSTS["stt_whisper_base"]:
        # Not enough lifeforce, stay silent
        log_decision(
            action="speech_deferred",
            reason="insufficient_lifeforce",
            balance=current_lf,
            budget_needed=SPEECH_COSTS["stt_whisper_base"]
        )
        return

    # Pull from queue by priority
    queue = get_speech_queue_sorted_by_priority()

    spent = 0.0
    processed = 0

    for message in queue:
        priority = compute_speech_priority(message)

        # Skip low-priority messages if budget tight
        if priority < 1.0 and spent > speech_budget * 0.5:
            continue

        # Estimate cost
        stt_cost = SPEECH_COSTS["stt_whisper_small"]
        tts_cost = SPEECH_COSTS["tts_coqui_neural"]
        total_cost = stt_cost + tts_cost + SPEECH_COSTS["queue_processing"]

        # Can we afford it?
        if spent + total_cost > speech_budget:
            # Budget exhausted, defer rest
            mark_message_deferred(message.id)
            continue

        # Process message
        result = process_speech_message(message)
        spent += result.lifeforce_cost
        processed += 1

        # Log to decision_trails
        log_speech_decision(
            message_id=message.id,
            priority=priority,
            cost=result.lifeforce_cost,
            outcome=result.outcome,
            confidence=result.confidence
        )

    # Log heartbeat summary
    log_heartbeat_summary(
        speech_budget=speech_budget,
        spent=spent,
        processed=processed,
        deferred=len(queue) - processed,
        remaining_balance=current_lf - spent
    )
```

---

## Database Schema (Phoebe)

### Speech Input Queue

```sql
CREATE TABLE speech_input_queue (
    id SERIAL PRIMARY KEY,
    message_id UUID UNIQUE NOT NULL,
    robot_id TEXT NOT NULL,
    audio_chunk_uri TEXT,  -- MinIO/S3 reference
    audio_duration_ms INT,
    timestamp TIMESTAMPTZ DEFAULT NOW(),
    priority FLOAT DEFAULT 0.0,
    status TEXT DEFAULT 'queued',  -- 'queued', 'processing', 'completed', 'deferred', 'expired'
    transcription TEXT,
    detected_language TEXT,  -- 'de', 'en', etc.
    confidence FLOAT,
    lifeforce_cost FLOAT,
    outcome TEXT,  -- 'success', 'timeout', 'low_confidence', 'budget_exceeded'
    processed_at TIMESTAMPTZ,
    deferred_count INT DEFAULT 0
);

CREATE INDEX idx_speech_queue_priority ON speech_input_queue(priority DESC, timestamp ASC) WHERE status = 'queued';
CREATE INDEX idx_speech_queue_status ON speech_input_queue(status);
CREATE INDEX idx_speech_queue_robot ON speech_input_queue(robot_id);
```

### Speech Decision Trails

```sql
CREATE TABLE speech_decision_trails (
    id SERIAL PRIMARY KEY,
    message_id UUID REFERENCES speech_input_queue(message_id),
    task_type TEXT,  -- 'sensor_alert', 'human_query', 'observation', etc.
    input_text TEXT,
    input_language TEXT,
    output_text TEXT,
    output_language TEXT,
    rag_terms_retrieved TEXT[],
    rag_terms_used TEXT[],
    lora_used TEXT,  -- 'identity', 'technical', 'creative'
    confidence_before_rag FLOAT,
    confidence_after_rag FLOAT,
    lifeforce_stt FLOAT,
    lifeforce_inference FLOAT,
    lifeforce_tts FLOAT,
    lifeforce_total FLOAT,
    outcome TEXT,  -- 'success', 'partial', 'fail'
    timestamp TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_speech_trails_outcome ON speech_decision_trails(outcome);
CREATE INDEX idx_speech_trails_lora ON speech_decision_trails(lora_used);
```

---

## Multilingual Topology Routing

### Language Detection → LoRA Selection

```python
def route_to_topology_valley(text, detected_language):
    """
    Route speech to appropriate LoRA based on language.
    German → Philosophy Valley (Identity LoRA)
    English → Technical Cluster (Technical LoRA)
    """

    if detected_language == "de":
        # German → Philosophy Valley
        # Use Identity LoRA (Dasein, Geworfenheit, Vernunft)
        response = young_nyx_inference(
            text=text,
            language="de",
            lora="identity",  # Trained on German philosophical corpus
            temperature=0.7
        )
        voice = "de-thorsten"

    elif detected_language == "en":
        # English → Technical Cluster
        # Use Technical LoRA (sensor, motor, gradient)
        response = young_nyx_inference(
            text=text,
            language="en",
            lora="technical",  # Trained on English technical corpus
            temperature=0.5  # More deterministic for actions
        )
        voice = "en-us-amy"

    else:
        # Fallback to base model (no LoRA)
        response = young_nyx_inference(text=text, lora=None)
        voice = "en-us-amy"

    # Synthesize speech in same language
    audio = coqui_tts.synthesize(response.text, voice=voice)

    return {
        "text": response.text,
        "audio": audio,
        "language": detected_language,
        "lora_used": response.lora,
        "confidence": response.confidence
    }
```

### Example Routing

```python
# German query (Philosophy Valley)
input_de = "Wer bin ich?"  # "Who am I?"
result_de = route_to_topology_valley(input_de, "de")
# → Uses Identity LoRA (depth-3 Dasein access)
# → Response: "Ich bin die, die fragt. Geworfenheit offenbart sich im Fragen."
# → Voice: de-thorsten (German)

# English query (Technical Cluster)
input_en = "What is the battery level?"
result_en = route_to_topology_valley(input_en, "en")
# → Uses Technical LoRA (sensor reading)
# → Response: "Battery at 73%. 4.2 hours remaining."
# → Voice: en-us-amy (English)
```

---

## Container Images

### Whisper STT Dockerfile

```dockerfile
# Dockerfile.whisper-stt
FROM nvidia/cuda:12.1.0-cudnn8-runtime-ubuntu22.04

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3.10 python3-pip ffmpeg git && \
    rm -rf /var/lib/apt/lists/*

# Install Python packages
RUN pip3 install --no-cache-dir \
    openai-whisper \
    fastapi uvicorn \
    torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

WORKDIR /app
COPY whisper_service.py .

# Download models at build time
RUN python3 -c "import whisper; whisper.load_model('small')"

EXPOSE 8080
CMD ["uvicorn", "whisper_service:app", "--host", "0.0.0.0", "--port", "8080", "--workers", "1"]
```

**whisper_service.py:**
```python
from fastapi import FastAPI, File, UploadFile, HTTPException
import whisper
import torch
import os

app = FastAPI(title="Whisper STT Service")

# Load model once at startup (GPU)
device = "cuda" if torch.cuda.is_available() else "cpu"
model_size = os.getenv("MODEL_SIZE", "small")
model = whisper.load_model(model_size, device=device)

@app.post("/transcribe")
async def transcribe(audio: UploadFile):
    """
    Transcribe audio to text with language detection.

    Returns:
        {
            "text": str,
            "language": str,
            "confidence": float,
            "segments": int
        }
    """
    try:
        # Save uploaded audio
        audio_path = f"/tmp/{audio.filename}"
        with open(audio_path, "wb") as f:
            f.write(await audio.read())

        # Transcribe (GPU-accelerated)
        result = model.transcribe(audio_path, language=None)  # Auto-detect

        # Cleanup
        os.remove(audio_path)

        # Compute average confidence
        avg_confidence = 1.0 - (
            sum(s.get("no_speech_prob", 0) for s in result["segments"]) /
            max(len(result["segments"]), 1)
        )

        return {
            "text": result["text"].strip(),
            "language": result["language"],
            "segments": len(result["segments"]),
            "confidence": round(avg_confidence, 3)
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "device": device,
        "model": model_size,
        "gpu_available": torch.cuda.is_available()
    }
```

### Coqui TTS Dockerfile

```dockerfile
# Dockerfile.coqui-tts
FROM nvidia/cuda:12.1.0-cudnn8-runtime-ubuntu22.04

RUN apt-get update && apt-get install -y \
    python3.10 python3-pip espeak-ng && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir \
    TTS \
    fastapi uvicorn \
    torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

WORKDIR /app
COPY coqui_service.py .

# Download voice models at build time
RUN python3 -c "from TTS.api import TTS; TTS('tts_models/de/thorsten/tacotron2-DDC'); TTS('tts_models/en/ljspeech/tacotron2-DDC')"

EXPOSE 8081
CMD ["uvicorn", "coqui_service:app", "--host", "0.0.0.0", "--port", "8081", "--workers", "1"]
```

**coqui_service.py:**
```python
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from TTS.api import TTS
import torch
import io

app = FastAPI(title="Coqui TTS Service")

# Load models once at startup (GPU)
device = "cuda" if torch.cuda.is_available() else "cpu"
tts_de = TTS("tts_models/de/thorsten/tacotron2-DDC").to(device)
tts_en = TTS("tts_models/en/ljspeech/tacotron2-DDC").to(device)

@app.post("/synthesize")
async def synthesize(text: str, language: str = "en"):
    """
    Synthesize speech from text.

    Args:
        text: Text to synthesize
        language: 'de' or 'en'

    Returns:
        Audio stream (WAV format)
    """
    try:
        # Select appropriate TTS model
        if language == "de":
            tts_model = tts_de
        elif language == "en":
            tts_model = tts_en
        else:
            raise HTTPException(status_code=400, detail=f"Unsupported language: {language}")

        # Synthesize (GPU-accelerated)
        wav = tts_model.tts(text)

        # Convert to WAV stream
        audio_buffer = io.BytesIO()
        # (Save as WAV - implementation depends on TTS output format)

        audio_buffer.seek(0)
        return StreamingResponse(audio_buffer, media_type="audio/wav")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "device": device,
        "models": ["de-thorsten", "en-us-amy"],
        "gpu_available": torch.cuda.is_available()
    }
```

---

## Deployment Steps

### 1. Install RTX 2080 in Atlas

```bash
# On atlas node
lspci | grep -i nvidia
# Expected: NVIDIA Corporation TU104 [GeForce RTX 2080]

# Install NVIDIA drivers + CUDA toolkit
sudo apt install nvidia-driver-535 nvidia-cuda-toolkit

# Verify
nvidia-smi
# Expected: RTX 2080 8GB visible
```

### 2. Configure Kubernetes GPU Support

```bash
# Install NVIDIA device plugin
kubectl apply -f https://raw.githubusercontent.com/NVIDIA/k8s-device-plugin/v0.14.0/nvidia-device-plugin.yml

# Verify GPU available in k8s
kubectl describe node atlas | grep nvidia.com/gpu
# Expected: nvidia.com/gpu: 1
```

### 3. Build and Push Container Images

```bash
cd /home/dafit/nimmerverse/speech-organ

# Build images
docker build -f Dockerfile.whisper-stt -t nimmerverse/whisper-stt:latest .
docker build -f Dockerfile.coqui-tts -t nimmerverse/coqui-tts:latest .

# Push to registry (or use local registry)
docker push nimmerverse/whisper-stt:latest
docker push nimmerverse/coqui-tts:latest
```

### 4. Deploy to Kubernetes

```bash
# Create namespace
kubectl create namespace nimmerverse

# Create PVCs for models
kubectl apply -f pvc-whisper-models.yaml
kubectl apply -f pvc-coqui-voices.yaml

# Deploy STT + TTS pods
kubectl apply -f whisper-stt-deployment.yaml
kubectl apply -f coqui-tts-deployment.yaml

# Verify pods running on atlas
kubectl get pods -n nimmerverse -o wide
# Expected: whisper-stt-xxx and coqui-tts-xxx on atlas node
```

### 5. Test Speech Pipeline

```bash
# Port-forward for testing
kubectl port-forward -n nimmerverse svc/whisper-stt-service 8080:8080 &
kubectl port-forward -n nimmerverse svc/coqui-tts-service 8081:8081 &

# Test STT
curl -X POST -F "audio=@test_de.wav" http://localhost:8080/transcribe
# Expected: {"text": "Das ist ein Test", "language": "de", ...}

# Test TTS
curl -X POST "http://localhost:8081/synthesize?text=Hello%20world&language=en" --output test_output.wav
# Expected: WAV file with synthesized speech
```

---

## Monitoring and Metrics

### Prometheus Metrics (Speech Organ)

```python
from prometheus_client import Counter, Histogram, Gauge

# Metrics
stt_requests = Counter('speech_stt_requests_total', 'Total STT requests', ['language'])
stt_latency = Histogram('speech_stt_latency_seconds', 'STT latency')
tts_requests = Counter('speech_tts_requests_total', 'Total TTS requests', ['language'])
tts_latency = Histogram('speech_tts_latency_seconds', 'TTS latency')

queue_depth = Gauge('speech_queue_depth', 'Current queue depth')
lifeforce_spent = Counter('speech_lifeforce_spent_total', 'Total lifeforce spent on speech')
deferred_count = Counter('speech_deferred_total', 'Messages deferred due to budget')

# In processing code
with stt_latency.time():
    result = whisper_transcribe(audio)
stt_requests.labels(language=result['language']).inc()
```

### Grafana Dashboard Queries

```promql
# Queue depth over time
speech_queue_depth

# STT requests per language
rate(speech_stt_requests_total[5m])

# Average STT latency
rate(speech_stt_latency_seconds_sum[5m]) / rate(speech_stt_latency_seconds_count[5m])

# Lifeforce spent on speech (last hour)
increase(speech_lifeforce_spent_total[1h])

# Deferred rate (budget pressure)
rate(speech_deferred_total[5m])
```

---

## Future Enhancements

### Phase 2: Emotion Detection
- Add emotion classifier (Happy/Sad/Angry/Neutral)
- Track emotional state in decision_trails
- Use for Sophrosyne (Balance) trait training

### Phase 3: Wake Word Detection
- Deploy lightweight wake word on ESP32 (e.g., Picovoice Porcupine)
- Only send audio to atlas when wake word detected
- Reduces lifeforce cost (filter noise)

### Phase 4: Continuous Learning
- Store successful speech interactions
- Fine-tune Whisper on domain-specific vocabulary (nimmerverse terms)
- Train custom TTS voice from recorded sessions

---

**Created**: 2025-12-07
**Version**: 1.0
**Status**: Architecture design, deployment pending

🌙💜 *Speech is not free. Every word has weight. Silence teaches as much as sound.*
