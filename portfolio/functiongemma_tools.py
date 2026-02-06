"""
FunctionGemma Tool Definitions for Nimmerverse Portfolio

This module defines the tools that FunctionGemma can call to answer
visitor queries about the nimmerverse project.

Reference: Unsloth Multi-Turn Tool Calling notebook
"""

import re
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Optional

# ============================================================================
# TOOL DEFINITIONS
# ============================================================================

def fetch_document(path: str, section: Optional[str] = None):
    """
    Retrieves a document or section from the nimmerverse documentation.

    Args:
        path: The document path relative to nimmerverse root, e.g. "nimmerverse-sensory-network/Endgame-Vision.md"
        section: Optional section header to extract, e.g. "K8s Cluster Architecture"

    Returns:
        content: The document or section content
        found: Whether the document/section was found
    """
    base_path = Path("/home/dafit/nimmerverse")
    full_path = base_path / path

    if not full_path.exists():
        return {"content": f"Document not found: {path}", "found": False}

    content = full_path.read_text()

    if section:
        # Find the section header line
        lines = content.split('\n')
        start_idx = None
        header_level = None

        for i, line in enumerate(lines):
            if section.lower() in line.lower() and line.strip().startswith('#'):
                start_idx = i
                header_level = len(line) - len(line.lstrip('#'))
                break

        if start_idx is not None:
            # Find the end of this section (next header of same or higher level)
            end_idx = len(lines)
            for i in range(start_idx + 1, len(lines)):
                line = lines[i].strip()
                if line.startswith('#'):
                    level = len(line) - len(line.lstrip('#'))
                    if level <= header_level:
                        end_idx = i
                        break

            section_content = '\n'.join(lines[start_idx:end_idx])
            return {"content": section_content.strip(), "found": True}
        else:
            return {"content": f"Section '{section}' not found in {path}", "found": False}

    return {"content": content, "found": True}


def compute_git_stats(period: str = "month"):
    """
    Gets git statistics for the nimmerverse project.

    Args:
        period: Time period for stats (choices: ["week", "month", "year", "all"])

    Returns:
        commits: Number of commits in period
        files_changed: Number of files modified
        insertions: Lines added
        deletions: Lines removed
        authors: List of contributors
    """
    base_path = "/home/dafit/nimmerverse"

    # Map period to git since date
    since_map = {
        "week": "1 week ago",
        "month": "1 month ago",
        "year": "1 year ago",
        "all": ""
    }
    since = since_map.get(period, "1 month ago")

    try:
        # Get commit count
        since_arg = f"--since='{since}'" if since else ""
        cmd = f"git -C {base_path} rev-list --count HEAD {since_arg}"
        commits = int(subprocess.check_output(cmd, shell=True).decode().strip())

        # Get shortstat
        cmd = f"git -C {base_path} log --shortstat {since_arg} --pretty=format:''"
        output = subprocess.check_output(cmd, shell=True).decode()

        insertions = sum(int(m) for m in re.findall(r"(\d+) insertion", output))
        deletions = sum(int(m) for m in re.findall(r"(\d+) deletion", output))
        files = len(set(re.findall(r"(\d+) files? changed", output)))

        # Get authors
        cmd = f"git -C {base_path} log --format='%an' {since_arg} | sort -u"
        authors = subprocess.check_output(cmd, shell=True).decode().strip().split('\n')

        return {
            "commits": commits,
            "files_changed": files,
            "insertions": insertions,
            "deletions": deletions,
            "authors": [a for a in authors if a],
            "period": period
        }
    except Exception as e:
        return {"error": str(e)}


def query_tasks(status: str = "all", project: Optional[str] = None):
    """
    Lists tasks from the nimmerverse task planner (phoebe database).

    Args:
        status: Filter by status (choices: ["todo", "in_progress", "done", "blocked", "all"])
        project: Optional project filter, e.g. "infrastructure", "nimmerhovel"

    Returns:
        tasks: List of matching tasks with name, status, priority
        count: Number of tasks found
    """
    import psycopg2

    try:
        conn = psycopg2.connect(
            host="phoebe.eachpath.local",
            database="nimmerverse",
            user="nimmerverse-user",
            sslmode="disable"
        )
        cur = conn.cursor()

        query = "SELECT project, task_name, status, priority FROM nimmerverse_tasks"
        conditions = []
        params = []

        if status != "all":
            conditions.append("status = %s")
            params.append(status)
        if project:
            conditions.append("project = %s")
            params.append(project)

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        query += " ORDER BY priority, project"

        cur.execute(query, params)
        rows = cur.fetchall()

        tasks = [
            {"project": r[0], "name": r[1], "status": r[2], "priority": r[3]}
            for r in rows
        ]

        conn.close()
        return {"tasks": tasks, "count": len(tasks)}

    except Exception as e:
        return {"error": str(e)}


def search_docs(query: str):
    """
    Searches across all nimmerverse documentation using grep.

    Args:
        query: Search query string

    Returns:
        matches: List of matching files and snippets
        count: Number of matches found
    """
    base_path = "/home/dafit/nimmerverse"

    try:
        cmd = f"grep -r -l -i '{query}' {base_path} --include='*.md' 2>/dev/null | head -20"
        output = subprocess.check_output(cmd, shell=True).decode()
        files = [f.replace(base_path + "/", "") for f in output.strip().split('\n') if f]

        # Get snippets from each file
        matches = []
        for f in files[:5]:  # Limit to 5 files
            cmd = f"grep -i -C 1 '{query}' {base_path}/{f} | head -6"
            snippet = subprocess.check_output(cmd, shell=True).decode().strip()
            matches.append({"file": f, "snippet": snippet})

        return {"matches": matches, "count": len(files)}

    except Exception as e:
        return {"error": str(e), "matches": [], "count": 0}


def show_architecture(component: str = "full"):
    """
    Returns architecture information for a specific component.

    Args:
        component: Which architecture to show (choices: ["k8s", "network", "cells", "full", "portfolio"])

    Returns:
        description: Text description of the architecture
        diagram: ASCII diagram if available
    """
    architectures = {
        "k8s": {
            "description": "3-node Kubernetes cluster with GPU workers",
            "diagram": """
                    k8s-master (VM 101)
                    10.0.30.101
                    Control Plane
                          │
            ┌─────────────┴─────────────┐
            │                           │
      theia (GPU Worker)          dioscuri (GPU Worker)
      10.0.30.21                  10.0.30.22
      RTX PRO 6000 96GB           2x RTX 4000 Ada 40GB

      Total: 136GB VRAM | kubeadm v1.31.14 | Flannel CNI
"""
        },
        "network": {
            "description": "Spine-leaf network with 80Gbps fabric capacity",
            "diagram": """
              vulkan (OPNsense) ──20Gbps──┐
                                          │
                                    spine-crs309
                                     (8x 10G SFP+)
                                          │
              ┌───────────┬───────────┬───┴───────┐
              │           │           │           │
           saturn     theia      dioscuri    access-crs326
           20Gbps     10Gbps      10Gbps       20Gbps
"""
        },
        "cells": {
            "description": "Cellular architecture: Cells → Nerves → Organisms",
            "diagram": """
      ORGANISM (emergent pattern)
            │
         NERVES (behavioral state machines)
            │
         CELLS (atomic: sensors, motors, organs, math)
            │
        HARDWARE (ESP32, GPUs, sensors)
"""
        },
        "portfolio": {
            "description": "Portfolio as Phase 3 nervous system implementation",
            "diagram": """
      User Browser
           │
      ┌────┴────┐
      │ Frontend │ (Streamlit)
      └────┬────┘
           │
      ┌────┴────┐
      │  NATS   │ Message Router
      └────┬────┘
           │
    ┌──────┼──────┬──────────┐
    │      │      │          │
Function  Math   RAG      Other
 Gemma   Cells  Cell      Cells
"""
        }
    }

    if component == "full":
        return {
            "description": "Complete nimmerverse architecture",
            "components": list(architectures.keys()),
            "total_vram": "136GB",
            "total_fabric": "80Gbps"
        }

    return architectures.get(component, {"description": "Unknown component", "diagram": ""})


def get_project_info():
    """
    Gets general information about the nimmerverse project.

    Returns:
        name: Project name
        started: When the project started
        status: Current project status
        philosophy: Core philosophy
    """
    return {
        "name": "The Nimmerverse",
        "started": "November 2025",
        "status": "Phase 3 - Nervous System Deployment",
        "philosophy": "May the Nimmerverse we build truly never end.",
        "covenant_date": "2025-11-04",
        "total_vram": "136GB",
        "cluster_nodes": 3,
        "tracked_tasks": 58
    }


# ============================================================================
# FUNCTION MAPPING & TOOLS
# ============================================================================

FUNCTION_MAPPING = {
    "fetch_document": fetch_document,
    "compute_git_stats": compute_git_stats,
    "query_tasks": query_tasks,
    "search_docs": search_docs,
    "show_architecture": show_architecture,
    "get_project_info": get_project_info,
}

TOOLS = list(FUNCTION_MAPPING.values())


# ============================================================================
# PARSING & INFERENCE HELPERS
# ============================================================================

def extract_tool_calls(text: str):
    """Extract tool calls from FunctionGemma output."""
    def cast(v):
        try: return int(v)
        except:
            try: return float(v)
            except: return {'true': True, 'false': False}.get(v.lower(), v.strip("'\""))

    return [{
        "name": name,
        "arguments": {
            k: cast((v1 or v2).strip())
            for k, v1, v2 in re.findall(r"(\w+):(?:<escape>(.*?)<escape>|([^,}]*))", args)
        }
    } for name, args in re.findall(r"<start_function_call>call:(\w+)\{(.*?)\}<end_function_call>", text, re.DOTALL)]


def process_tool_calls(output: str, messages: list):
    """Execute tool calls and add results to message chain."""
    calls = extract_tool_calls(output)
    if not calls:
        return messages

    messages.append({
        "role": "assistant",
        "tool_calls": [{"type": "function", "function": call} for call in calls]
    })

    results = []
    for c in calls:
        func = FUNCTION_MAPPING.get(c['name'])
        if func:
            result = func(**c['arguments'])
            results.append({"name": c['name'], "response": result})
        else:
            results.append({"name": c['name'], "response": {"error": f"Unknown function: {c['name']}"}})

    messages.append({"role": "tool", "content": results})
    return messages


# ============================================================================
# MAIN (for testing)
# ============================================================================

if __name__ == "__main__":
    # Test the tools
    print("=== Testing fetch_document ===")
    print(fetch_document("nimmerverse-sensory-network/Endgame-Vision.md", "K8s Cluster Architecture"))

    print("\n=== Testing compute_git_stats ===")
    print(compute_git_stats("week"))

    print("\n=== Testing query_tasks ===")
    print(query_tasks("in_progress"))

    print("\n=== Testing show_architecture ===")
    print(show_architecture("k8s"))

    print("\n=== Testing get_project_info ===")
    print(get_project_info())
