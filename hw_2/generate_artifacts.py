#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys
from PIL import Image

from hw_2 import build_document, generate_figure, generate_table


ARTIFACTS_DIR = Path(__file__).parent / "artifacts"
PNG_PATH = ARTIFACTS_DIR / "sample.png"
TEX_PATH = ARTIFACTS_DIR / "example.tex"
PDF_PATH = ARTIFACTS_DIR / "example.pdf"


def ensure_artifacts_dir() -> None:
    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)


def write_sample_png() -> None:
    img = Image.new("RGB", (100, 100), color="red")
    PNG_PATH.parent.mkdir(parents=True, exist_ok=True)
    img.save(PNG_PATH, "PNG")


def build_example_tex() -> None:
    table_block = generate_table(
        data=[["Фамилия", "Имя"], ["Рудаков", "Никита"]],
        caption="Таблица с фамилией и именем",
        label="tab:sample",
        alignment="lc",
    )

    figure_block = generate_figure(
        image_path=PNG_PATH.name,
        caption="Красный квадрат",
        label="fig:sample",
        width="0.3\\textwidth",
    )

    document = build_document(
        body_blocks=[table_block, figure_block],
        title="HW2: LaTeX generation",
        author="",
    )
    TEX_PATH.write_text(document, encoding="utf-8")


def build_pdf() -> None:
    if not TEX_PATH.exists():
        build_example_tex()
    try:
        result = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", TEX_PATH.name],
            cwd=ARTIFACTS_DIR,
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        output = result.stdout.decode("utf-8", errors="replace")
        # Если PDF создан, считаем успешным даже при ненулевом коде возврата
        if PDF_PATH.exists():
            return
        # Если PDF не создан, выводим ошибку
        raise RuntimeError(f"PDF не сгенерирован. Вывод pdflatex:\n{output}")
    except FileNotFoundError as exc:
        raise RuntimeError("pdflatex не установлен, установите TeXLive") from exc


def main() -> None:
    ensure_artifacts_dir()
    write_sample_png()
    build_example_tex()
    if "--pdf" in sys.argv:
        build_pdf()


if __name__ == "__main__":
    main()

