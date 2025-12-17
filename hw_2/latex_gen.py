from typing import Iterable, List, Optional


def generate_table(
    data: Iterable[Iterable],
    caption: Optional[str] = None,
    label: Optional[str] = None,
    alignment: Optional[str] = None,
) -> str:
    rows: List[List[str]] = [[str(cell) for cell in row] for row in data]
    if not rows:
        raise ValueError("table data is empty")

    cols_count = len(rows[0])
    if any(len(row) != cols_count for row in rows):
        raise ValueError("all rows must have equal length")

    column_spec = alignment or ("l" * cols_count)
    body = " \\\\\n".join([" & ".join(row) for row in rows])

    caption_block = f"\\caption{{{caption}}}\n" if caption else ""
    label_block = f"\\label{{{label}}}\n" if label else ""

    return (
        "\\begin{table}[h]\n"
        "\\centering\n"
        f"\\begin{{tabular}}{{{column_spec}}}\n"
        "\\hline\n"
        f"{body} \\\\\n"
        "\\hline\n"
        "\\end{tabular}\n"
        f"{caption_block}"
        f"{label_block}"
        "\\end{table}\n"
    )


def generate_figure(
    image_path: str,
    caption: Optional[str] = None,
    label: Optional[str] = None,
    width: str = "0.6\\textwidth",
) -> str:
    caption_block = f"\\caption{{{caption}}}\n" if caption else ""
    label_block = f"\\label{{{label}}}\n" if label else ""

    return (
        "\\begin{figure}[h]\n"
        "\\centering\n"
        f"\\includegraphics[width={width}]{{{image_path}}}\n"
        f"{caption_block}"
        f"{label_block}"
        "\\end{figure}\n"
    )


def build_document(
    body_blocks: Iterable[str],
    title: Optional[str] = None,
    author: Optional[str] = None,
) -> str:
    body = "\n".join(body_blocks)
    if title:
        title_block = f"\\title{{{title}}}\n"
        author_block = f"\\author{{{author}}}\n" if author else "\\author{}\n"
        title_block += author_block + "\\maketitle\n"
    else:
        title_block = ""

    return (
        "\\documentclass{article}\n"
        "\\usepackage[utf8]{inputenc}\n"
        "\\usepackage[T2A]{fontenc}\n"
        "\\usepackage[russian]{babel}\n"
        "\\usepackage{graphicx}\n"
        "\\usepackage{array}\n"
        "\\begin{document}\n"
        f"{title_block}"
        f"{body}\n"
        "\\end{document}\n"
    )
