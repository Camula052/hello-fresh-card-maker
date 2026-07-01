import fitz
from PIL import Image
from recipe import Recipe

def load_pdf(path):
    return fitz.open(path)


def render_page(pdf, page_number, zoom=2):
    page = pdf.load_page(page_number)

    matrix = fitz.Matrix(zoom, zoom)

    pix = page.get_pixmap(matrix=matrix)

    image = Image.frombytes(
        "RGB",
        [pix.width, pix.height],
        pix.samples
    )

    return image

def analyze_pdf(pdf):

    page1 = pdf.load_page(0)

    data = page1.get_text("dict")

    print("=" * 60)

    print("TEXTBLÖCKE")

    print("=" * 60)

    for block in data["blocks"]:

        if "lines" not in block:
            continue

        text = ""

        for line in block["lines"]:
            for span in line["spans"]:
                text += span["text"]

        if text.strip():
            print(text)

    print("=" * 60)

    print("BILDER")

    print("=" * 60)

    images = page1.get_images()

    print(f"{len(images)} Bilder gefunden")