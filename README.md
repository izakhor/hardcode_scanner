# 🔐 Secret Scanner (Python)

Un **scanner de secrets et hardcoded credentials** écrit en Python.  
Il permet de détecter des mots de passe, API keys, tokens et autres secrets potentiellement exposés dans un dépôt ou un dossier.

👉 Projet personnel orienté **cybersécurité**

---

## 🚀 Fonctionnalités

- 🔍 Scan récursif de dossiers
- 🧠 Détection de secrets hardcodés via regex
- 🧪 Distinction entre **valeurs de test** et **secrets réels**
- 📊 Attribution d’un niveau de sévérité (`High`, `Low`)
- 📄 Export d’un **rapport JSON structuré**
- 🗂️ Support de plusieurs types de fichiers :
  - `.py`, `.js`, `.ts`
  - `.env`
  - `.yml`, `.yaml`
  - `.json`, `.txt`

---

## 🧠 Détection des secrets

Le scanner recherche des patterns courants comme :

- `api_key`
- `apikey`
- `secret`
- `token`
- `password`
- `passwd`
- `pwd`
- `db_password`
- `dbpassword`

Exemple détecté :

```python
api_key = "UwoEtNGJ3Xk8hh9H_vhs0VRVfQkn1vg0j52MGQ8tiwbg1nAKsQu9"
```
Les valeurs connues comme test, changeme, 1234, etc. sont automatiquement classées en sévérité basse.

# 📄 Exemple de rapport JSON
```json
"scan_info": {
        "files_scanned": 6,
        "secrets_found": 1
    },
    "findings": [
        {
            "file": "/home/user/Documents/hardcode/abc/aaaa.txt",
            "line_number": 2,
            "severity": "High",
            "keyword": "password",
            "value": "Mon****23",
            "value_hash": "e0c19fe52619f6b0e176812390bc0a916dce561e13be12acb6766aa58eeb5ffa",
            "reason": "Possible Hardcode detected !"
        }
```

# ▶️ Utilisation:
```python
python hardcode_scanner.py <path> --export <json_output>
```

🔐 Limites connues

- Pas encore de faux positifs avancés

- Pas de scan de secrets encodés (Base64, etc.)


- Pas d’intégration CI automatique (GitHub Actions)




