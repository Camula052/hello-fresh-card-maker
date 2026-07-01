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

def parse_recipe(pdf):

    recipe = Recipe()

    page1 = pdf.load_page(0)

    recipe.title = parse_title(page1)

    return recipe

def parse_title(page):

    data = page.get_text("dict")

    longest = ""

    for block in data["blocks"]:

        if "lines" not in block:
            continue

        text = ""

        for line in block["lines"]:
            for span in line["spans"]:
                text += span["text"]

        text = text.strip()

        if len(text) > len(longest):
            longest = text

    return longest