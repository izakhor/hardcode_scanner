# 🔐 Secret Scanner (Python)

Un **scanner de secrets et hardcoded credentials** écrit en Python.  
Il permet de détecter des mots de passe, API keys, tokens et autres secrets potentiellement exposés dans un dépôt ou un dossier.

👉 Projet orienté **cybersécurité / SAST léger**, pensé pour être **CI-ready** et lisible par des recruteurs.

---

## 🚀 Fonctionnalités

- 🔍 Scan récursif de dossiers
- 🧠 Détection de secrets hardcodés via regex
- 🧪 Distinction entre **valeurs de test** et **secrets réels**
- 📊 Attribution d’un niveau de sévérité (`High`, `Low`)
- 📄 Export d’un **rapport JSON structuré**
- 🗂️ Support de plusieurs types de fichiers :
  - `.py`, `.js`, `.ts`
  - `.yml`, `.yaml`
  - `.json`, `.txt`

---

## 📁 Structure du projet

Hardcode-Scanner/
├── hardcode/
│ ├── test.txt
│ ├── bar.py
│ └── ...
├── scanner.py
├── scanner_report.json
└── README.md

---

## 🧠 Détection des secrets

Le scanner recherche des patterns courants comme :

- `api_key`
- `apikey`
- `secret`
- `token`
- `password`
- `db_password`

Exemple détecté :

```python
api_key = "UwoEtNGJ3Xk8hh9H_vhs0VRVfQkn1vg0j52MGQ8tiwbg1nAKsQu9"

Les valeurs connues comme test, changeme, 1234, etc. sont automatiquement classées en sévérité basse.

Exemple de rapport JSON

"scan_info": {
        "files_scanned": 6,
        "secrets_found": 3
    },
    "findings": [
        {
            "file": "/home/seika/Documents/hardcode/abc/aaaa.txt",
            "line_number": 2,
            "severity": "High",
            "keyword": "password",
            "value": "Mon****23",
            "value_hash": "e0c19fe52619f6b0e176812390bc0a916dce561e13be12acb6766aa58eeb5ffa",
            "reason": "Possible Hardcode detected !"
        }


Utilisation:

"python hardcode_scanner.py <path> --export <json_output>"

🔐 Limites connues

- Pas encore de faux positifs avancés

- Pas de scan de secrets encodés (Base64, etc.)

- Pas d’intégration CI automatique (GitHub Actions)