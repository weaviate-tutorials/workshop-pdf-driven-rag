from pathlib import Path
from pdf2image import convert_from_path
import math


def convert_pdf_to_images(src_file_path: Path, img_path: Path) -> list[Path]:
    tgt_file_path_prefix = src_file_path.stem
    images = convert_from_path(str(src_file_path))

    img_path.mkdir(parents=True, exist_ok=True)

    digits = int(math.log10(len(images))) + 1
    img_paths = []

    for i, img in enumerate(images, start=1):
        img_file_path = (
            img_path / f"{tgt_file_path_prefix}_{i:0{digits}d}_of_{len(images)}.png"
        )
        img.save(img_file_path, "PNG")
        img_paths.append(img_file_path)

    return img_paths


pdf_path = Path("data/pdfs/manual_bosch_WGG254Z0GR.pdf")
img_dir = Path("data/imgs")

convert_pdf_to_images(pdf_path, img_dir)
