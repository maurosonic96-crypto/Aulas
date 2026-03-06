Usando o copilot para transformar o pdf da aula em arquivo markdown (.md).
Dificuldades encontradas:
*configuração do git (nome e e-mail)
*baixa familiaridade com os termos técnicos do git
*publicação em branches ao invés de pastas (repositórios bagunçados)

# PDF → Markdown converter

Requirements:

- Python 3.8+
- Install dependency:

```powershell
python -m pip install pypdf
```

Usage:

```powershell
python scripts\pdf_to_md.py "d:\atividade_aula_3_git\Aula 03 - Conceitos, Funções e Tipos de Sistemas Operacionais.pdf"
```

Optional: provide `-o output.md` to set the output path.

The script extracts text pages and writes a simple Markdown file next to the PDF (same base name).
