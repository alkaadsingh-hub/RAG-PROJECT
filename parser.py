#Text and image extraction

import fitz  # PyMuPDF
import os

def extract_text_and_images(pdf_path):
    doc = fitz.open(pdf_path)

    os.makedirs("data/markdown", exist_ok=True)
    os.makedirs("data/images", exist_ok=True)

    all_pages_text = []

    for page_num, page in enumerate(doc):
        text = page.get_text()

        # Save text as markdown
        with open(f"data/markdown/page_{page_num}.md", "w", encoding="utf-8") as f:
            f.write(text)

        all_pages_text.append({
            "content": text,
            "metadata": {"type": "text", "page": page_num}
        })

        # Extract images
        image_list = page.get_images(full=True)

        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]

            img_path = f"data/images/page_{page_num}_img_{img_index}.png"
            with open(img_path, "wb") as f:
                f.write(image_bytes)

    return all_pages_text