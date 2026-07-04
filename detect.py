#!/usr/bin/env python3
"""
Project type detection utility for localhost-to-wifi skill.
Identifies framework and provides configuration guidance.
"""

import json
import os
from pathlib import Path

def detect_project_type(root_path="."):
    """
    Detect the project framework based on files in the root directory.
    Returns a dict with detected framework and relevant files.
    """
    root = Path(root_path)
    detected = {
        "framework": "unknown",
        "files_found": [],
        "config": {}
    }
    
    # Check for various framework indicators
    files_to_check = {
        "package.json": "node",
        "requirements.txt": "python",
        "pyproject.toml": "python",
        "setup.py": "python",
        "Pipfile": "python",
        "next.config.js": "nextjs",
        "next.config.ts": "nextjs",
        "vite.config.js": "vite",
        "vite.config.ts": "vite",
        "tsconfig.json": "typescript",
        "wsgi.py": "flask",
        "asgi.py": "django",
        "manage.py": "django",
    }
    
    # Scan files
    found_files = {}
    for filename, framework_hint in files_to_check.items():
        if (root / filename).exists():
            found_files[filename] = framework_hint
            detected["files_found"].append(filename)
    
    # Determine framework
    if "package.json" in found_files:
        if "next.config.js" in found_files or "next.config.ts" in found_files:
            detected["framework"] = "nextjs"
        elif "vite.config.js" in found_files or "vite.config.ts" in found_files:
            detected["framework"] = "vite"
        else:
            # Check package.json for framework clues
            try:
                with open(root / "package.json") as f:
                    pkg = json.load(f)
                    if "fastapi" in str(pkg.get("dependencies", {})):
                        detected["framework"] = "fastapi"
                    elif "express" in str(pkg.get("dependencies", {})):
                        detected["framework"] = "express"
                    elif "react" in str(pkg.get("dependencies", {})):
                        detected["framework"] = "react"
                    else:
                        detected["framework"] = "nodejs"
            except:
                detected["framework"] = "nodejs"
    
    elif "pyproject.toml" in found_files or "requirements.txt" in found_files:
        # Python project - check for specific frameworks
        req_files = []
        if (root / "requirements.txt").exists():
            with open(root / "requirements.txt") as f:
                reqs = f.read().lower()
                if "fastapi" in reqs or "uvicorn" in reqs:
                    detected["framework"] = "fastapi"
                elif "flask" in reqs:
                    detected["framework"] = "flask"
                elif "django" in reqs:
                    detected["framework"] = "django"
                else:
                    detected["framework"] = "python"
        
        elif (root / "pyproject.toml").exists():
            with open(root / "pyproject.toml") as f:
                content = f.read().lower()
                if "fastapi" in content:
                    detected["framework"] = "fastapi"
                elif "flask" in content:
                    detected["framework"] = "flask"
                elif "django" in content:
                    detected["framework"] = "django"
                else:
                    detected["framework"] = "python"
    
    return detected

def get_config_instructions(framework):
    """
    Return configuration instructions for the detected framework.
    """
    instructions = {
        "nextjs": {
            "port": 3000,
            "command": "npm run dev -- -H 0.0.0.0",
            "config_file": "next.config.js",
            "code_example": """// In next.config.js
module.exports = {
  server: {
    host: '0.0.0.0'
  }
}"""
        },
        "vite": {
            "port": 5173,
            "command": "npm run dev -- --host",
            "config_file": "vite.config.js",
            "code_example": """// In vite.config.js
import { defineConfig } from 'vite'
export default defineConfig({
  server: {
    host: '0.0.0.0',
    port: 5173
  }
})"""
        },
        "express": {
            "port": 3000,
            "command": "node server.js",
            "config_file": "server.js",
            "code_example": """// In your main server file
app.listen(3000, '0.0.0.0', () => {
  console.log('Server running on 0.0.0.0:3000');
});"""
        },
        "fastapi": {
            "port": 8000,
            "command": "uvicorn main:app --host 0.0.0.0 --port 8000 --reload",
            "config_file": "main.py",
            "code_example": """# In main.py
if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)"""
        },
        "flask": {
            "port": 5000,
            "command": "python app.py",
            "config_file": "app.py",
            "code_example": """# In app.py
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)"""
        },
        "django": {
            "port": 8000,
            "command": "python manage.py runserver 0.0.0.0:8000",
            "config_file": "manage.py",
            "code_example": "python manage.py runserver 0.0.0.0:8000"
        }
    }
    
    return instructions.get(framework, instructions.get("nodejs", {}))

if __name__ == "__main__":
    import sys
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    detected = detect_project_type(path)
    framework = detected["framework"]
    instructions = get_config_instructions(framework)
    
    print(f"Detected Framework: {framework}")
    print(f"Files Found: {', '.join(detected['files_found'])}")
    print(f"\nDefault Port: {instructions.get('port', 'varies')}")
    print(f"Start Command: {instructions.get('command', 'varies')}")
    print(f"\nCode to update in {instructions.get('config_file', 'your config file')}:")
    print(instructions.get('code_example', 'See SKILL.md for details'))
