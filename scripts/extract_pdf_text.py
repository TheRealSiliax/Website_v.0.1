import os
import sys


def main() -> int:
    try:
        from pdfminer.high_level import extract_text  # type: ignore
    except Exception as import_error:  # pragma: no cover
        sys.stderr.write(f"Fehler: pdfminer.six nicht installiert oder Importproblem: {import_error}\n")
        return 2

    script_dir = os.path.abspath(os.path.dirname(__file__))
    base_dir = os.path.abspath(os.path.join(script_dir, os.pardir))

    pdf_path = os.path.join(base_dir, "#01 Agentnetzwerk Testprojekt 1.pdf")
    out_dir = os.path.join(base_dir, "docs", "intake")
    out_path = os.path.join(out_dir, "testprojekt1.md")

    os.makedirs(out_dir, exist_ok=True)

    if not os.path.exists(pdf_path):
        sys.stderr.write(f"Fehler: PDF nicht gefunden: {pdf_path}\n")
        return 3

    try:
        text = extract_text(pdf_path)
    except Exception as extract_error:
        sys.stderr.write(f"Fehler bei der Textextraktion: {extract_error}\n")
        return 4

    try:
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text)
    except Exception as write_error:
        sys.stderr.write(f"Fehler beim Schreiben der Ausgabedatei: {write_error}\n")
        return 5

    print(f"OK: Extrahiert nach {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


