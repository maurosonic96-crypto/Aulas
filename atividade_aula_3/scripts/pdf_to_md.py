import argparse
import os
import re
from pypdf import PdfReader


def extract_text_from_pdf(path: str) -> str:
    reader = PdfReader(path)
    parts = []
    for page in reader.pages:
        text = page.extract_text() or ""
        parts.append(text)
    full = "\n\n".join(parts)
    return full


def simple_cleanup(text: str) -> str:
    # Normalize line endings
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    # Collapse consecutive blank lines to two (markdown paragraph)
    text = re.sub(r"\n{3,}", "\n\n", text)
    # Trim trailing/leading whitespace
    text = text.strip()
    return text


def make_markdown(text: str, title: str = None) -> str:
    md_parts = []
    if title:
        md_parts.append(f"# {title}")
    md_parts.append(text)
    return "\n\n".join(md_parts)


def main():
    p = argparse.ArgumentParser(description="Convert PDF to simple Markdown by extracting text.")
    p.add_argument("input", help="Input PDF file path")
    p.add_argument("-o", "--output", help="Output markdown file path (optional)")
    args = p.parse_args()

    inp = args.input
    if not os.path.isfile(inp):
        print(f"Input file not found: {inp}")
        raise SystemExit(2)

    raw = extract_text_from_pdf(inp)
    cleaned = simple_cleanup(raw)
    base = os.path.splitext(os.path.basename(inp))[0]
    md = make_markdown(cleaned, title=base)

    out = args.output or os.path.join(os.path.dirname(inp), base + ".md")
    with open(out, "w", encoding="utf-8") as f:
        f.write(md)

    print(f"Wrote: {out}")


if __name__ == "__main__":
    main()
