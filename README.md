# Website Projekt

Dieses Projekt verwendet ein Agent-AI-Team Framework für strukturierte Entwicklung.

## GitHub Backup

Das Projekt ist mit GitHub verbunden für automatische Backups.

### Repository
- **URL**: https://github.com/TheRealSiliax/Website_v.0.1.git

### Backup durchführen

Um eine Sicherung zu erstellen, sag einfach:
- "Sicherung machen"
- "Backup erstellen"
- "in GitHub sichern"
- "zu GitHub hochladen"

Der Orchestrator erkennt diese Anfragen automatisch und leitet sie an den Backup-Agenten weiter.

### Manuelle Backup-Ausführung

Falls du das Backup manuell ausführen möchtest:

```bash
python scripts/github_backup.py
```

### Konfiguration

Die GitHub-Konfiguration befindet sich in `.github_config.yaml`. Stelle sicher, dass:
- `repository_url` korrekt gesetzt ist
- `git_user_name` und `git_user_email` deine Git-Konfiguration widerspiegeln
- Authentifizierung eingerichtet ist (SSH-Keys oder Personal Access Token)

### Authentifizierung

Für die Authentifizierung mit GitHub empfehlen wir:
1. **SSH-Keys** (empfohlen): Einfach SSH-Key zu GitHub hinzufügen
2. **Personal Access Token**: Als Umgebungsvariable setzen
3. **Git Credential Manager**: Automatische Verwaltung

## Projektstruktur

- `framework/`: Agent-AI-Team Framework
- `docs/`: Projektdokumentation
- `scripts/`: Utility-Scripts
- `.github_config.yaml`: GitHub-Konfiguration

Siehe `docs/README.md` für weitere Informationen zum Framework.

