### Tool-Registry

Verzeichnis unterstützter Tools/Integrationen mit Zweck, Inputs/Outputs, Beispielaufrufen.

Template pro Tool:

```
- name: <Toolname>
  purpose: <Wofür wird es genutzt>
  inputs: <Input-Formate>
  outputs: <Output-Formate>
  usage: <Kurzbeispiel>
```

## GitHub Backup Tool

- **name**: github_backup
- **purpose**: Führt automatische Sicherungen des Projekts in das konfigurierte GitHub-Repository durch
- **inputs**: 
  - `.github_config.yaml` (Repository-URL, Git-Konfiguration)
  - Projekt-Dateien (respektiert `.gitignore`)
- **outputs**: 
  - Backup-Status (Erfolg/Fehler)
  - Commit-Hash und Timestamp
  - Git-Push zu GitHub
- **usage**: 
  ```bash
  python scripts/github_backup.py
  ```
- **Konfiguration**: Siehe `.github_config.yaml` im Projekt-Root
- **Agent**: Wird vom Backup-Agent (`framework/agents/backup.md`) verwendet


