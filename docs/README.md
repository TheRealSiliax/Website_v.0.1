### Projektdokumentation

Dieser Ordner dient als zentrale Wissensbasis für das Projekt. Nutze diese Seite als Startpunkt, um bisherige Arbeitsergebnisse, Entscheidungen und Ressourcen schnell zu finden.

---

### Inhaltsverzeichnis
- [Arbeitsprotokoll (Sessions)](#arbeitsprotokoll-sessions)
- [Entscheidungslog (ADR-light)](#entscheidungslog-adr-light)
- [Artefakte & Ressourcen](#artefakte--ressourcen)
- [Tools, Agenten & Operator-Befehle](#tools-agenten--operator-befehle)

---

### Arbeitsprotokoll (Sessions)
Pro Sitzungsstart einen Eintrag am Anfang ergänzen (neustes zuerst).

Template:

```
## YYYY-MM-DD — Kurzbeschreibung der Sitzung
- Ziele: ...
- Ergebnis: ...
- Nächste Schritte: ...
```

**Aktuelle Sitzung**: [2025-08-20 — Framework-Aufbau](docs/sessions/2025-08-20_bba28ee9-bbe3-4786-ad07-26ebb53618c6.md)

---

### Entscheidungslog (ADR-light)
Wichtige Architektur-/Produktentscheidungen festhalten.

Template:

```
## ADR-<laufende Nummer>: Entscheidungstitel (YYYY-MM-DD)
- Kontext: ...
- Entscheidung: ...
- Alternativen: ...
- Konsequenzen: ...
```

---

### Artefakte & Ressourcen
- **Framework**: Vollständige Agent-AI-Team-Struktur unter `framework/`
  - 7 spezialisierte Agenten (Orchestrator, Research, Code, Architect, Debug, Ask, Memory)
  - Boomerang-Loop für Delegation ↔ Reporting
  - 6 Phasen-SOPs (Intake → Research → Planning → Implementation → Review → Handover)
  - Primitive Operators (10 kognitive Grundoperationen)
  - Templates für Tasks, Reporter, ADRs
- **Intake**: PDF-Extrakt `docs/intake/testprojekt1.md` (SPARC-System)
- **Sessions**: Chronologische Sitzungsnotizen
- **ADRs**: Architektur-Entscheidungsprotokolle

---

### Tools, Agenten & Operator-Befehle
Nutze den Operator-Block in `Cursor.md` zu Beginn jeder Session. Vorschlag für kurze Operator-Befehle:

```
- Kontext laden: Öffne `docs/README.md` und fasse die letzten 3 Sitzungen zusammen.
- Aufgaben ableiten: Erzeuge eine To-do-Liste aus den offenen Punkten der letzten Sitzung.
- Entscheidung prüfen: Liste offene ADRs und schlage nächste Schritte vor.
- Framework nutzen: Starte mit Orchestrator → Research → Code/Architect je nach Aufgabe.
```

**Framework-Startpunkt**: [framework/README.md](framework/README.md)

**🚀 Für Anfänger**: [Quickstart-Anleitung](framework/guides/quickstart.md) - So einfach wie ein Spiel mit Bauklötzen!

**📋 Step-by-Step-Anleitung**: [Schnellstart auf der obersten Ebene](../Step-by-Step-Anleitung/README.md) - Die wichtigste Anleitung für den Start!


