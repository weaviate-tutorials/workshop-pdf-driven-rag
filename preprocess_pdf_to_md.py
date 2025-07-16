from pathlib import Path
from docling.document_converter import DocumentConverter


def parse_pdf(input_doc_path: Path, output_dir: Path):
    doc_converter = DocumentConverter()
    conv_res = doc_converter.convert(input_doc_path)

    # Save markdown
    filename = input_doc_path.stem
    md_filepath = output_dir / f"{filename}-parsed-text.md"
    print(f"Saving parsed text to {md_filepath}")
    with md_filepath.open("w", encoding="utf-8") as md_file:
        md_file.write(conv_res.document.export_to_markdown())


data_folder = Path("data/pdfs")
output_dir = Path("data/parsed")
output_dir.mkdir(parents=True, exist_ok=True)

for pdf_path in data_folder.glob("*.pdf"):
    print(f"Processing {pdf_path.name}...")
    parse_pdf(pdf_path, output_dir)
