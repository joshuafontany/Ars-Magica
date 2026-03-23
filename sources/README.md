# Source PDFs

Place owned Ars Magica PDFs in `~/Ars-Magica/_books/`.

Expected workflow:

1. Drop source PDFs into `_books/` using slug-based filenames that match `catalog.yml`.
2. Run the ingestion script from the repo root.
3. Review generated chapter Markdown and errata pages before publishing.

## Naming Convention

Normalize source files to:

- `ars-magica-5th-edition-standard-core-rulebook.pdf`
- `realms-of-power-magic.pdf`
- `realms-of-power-faerie.pdf`

Do not commit PDFs, OCR caches, or raw extraction artifacts.
