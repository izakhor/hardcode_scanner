import os
import re
import json
import sys
import hashlib


t_pattern = re.compile(r"(?P<key>api_key|apikey|secret|token|password|passwd|pwd|db_password|dbpassword)\s*(=|:|:=)\s*[\"']?(?P<value>[^\"']+)[\"']?", re.IGNORECASE)
test_words = {"test", "changeme", "example", "password", "1234", "abc123","demo", "dummy", "fake", "placeholder", "secret", "motdepasse"}

def mask_value(value):
    if len(value) <= 6:
        return "***"
    return value[:3] + "****" + value[-2:]

def detect_secret(line, line_no, file_path):
    t_match = t_pattern.search(line)

    stripped = line.strip()
    if stripped.startswith(("#", "//")):
        return None
        
    if not t_match:
        return None
    
    key = t_match.group("key")
    value = t_match.group("value")
    if any(word in value.lower() for word in test_words):
        severity = "Low"
        reason = "Possible Test value"
    else:
        severity = "High"
        reason = "Possible Hardcode detected !"
    
    return {
        "file": file_path,
        "line_number": line_no,
        "severity": severity,
        "keyword": key,
        "value_preview": mask_value(value),
        "value_hash": hashlib.sha256(value.encode()).hexdigest(),
        "reason": reason
    }

def scan_files(file_path):
    findings = []
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            for i,line in enumerate(f,start=1):
                result = detect_secret(line,i,file_path)
                if result:
                    findings.append(result)
    except Exception as e:
        print(f"[!] Erreur lecture {file_path}: {e}")
    return findings


def scan_dir(path,output_file):
    all_findings = []
    files_scanned = 0

    ext = [".py", ".js", ".env", ".ts", ".yml", ".yaml", ".json", ".txt"]
    IGNORE_DIRS = {".git", "venv", "__pycache__", "node_modules"}

    for root, subdirs, files in os.walk(path):
        subdirs[:] = [d for d in subdirs if d not in IGNORE_DIRS]

        for f in files:
            if os.path.splitext(f)[1] not in ext:
                continue

            full_path = os.path.join(root, f)
            files_scanned += 1

            findings = scan_files(full_path)
            all_findings.extend(findings)

    report = {
        "scan_info": {
            "files_scanned": files_scanned,
            "secrets_found": len(all_findings)
        },
        "findings": all_findings
    }

    export_file(report,output_file)


def export_file(result,output_file):
    with open(output_file, "w") as f:
        json.dump(result, f, indent=4)


if __name__ == "__main__":

    if len(sys.argv) < 3 or len(sys.argv) > 4 or sys.argv[2] != "--export":
        print("Usage: python.exe hardcode_scanner.py <directory_path> --export <output_file>")
        sys.exit(1)
    else: 
        path = sys.argv[1]
        output_file = sys.argv[3]
        scan_dir(path, output_file)