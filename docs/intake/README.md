### Intake: Quellmaterial erfassen

Hier kommen Rohinhalte (z. B. aus PDFs) als Text/Markdown rein, bevor sie in Rollen, Prozesse und SOPs überführt werden.

#### Vorgehen
1) PDF-Text extrahieren und als `.md` hier ablegen (z. B. `testprojekt1.md`).
2) Inhalte grob gliedern (Rollen, Prozesse, Artefakte, Checklisten).
3) Relevantes in `framework/` überführen (Rollen, SOPs, Prozesse, Templates).

#### Optionen zum Extrahieren (manuell oder skriptiert)
- Manuell: PDF öffnen, Textabschnitte kopieren, hier einfügen.
- PowerShell (mit Python):
  - `python -m pip install pdfminer.six`
  - `python -c "from pdfminer.high_level import extract_text; import sys; open('docs/intake/testprojekt1.md','w',encoding='utf-8').write(extract_text('#01 Agentnetzwerk Testprojekt 1.pdf'))"`
  
Falls Python nicht verfügbar ist, sag Bescheid – ich biete eine Alternative an.


