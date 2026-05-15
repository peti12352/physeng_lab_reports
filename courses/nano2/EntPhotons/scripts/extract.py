import os
import pymupdf4llm

pdf_path = "EntPhotons.pdf"
out_dir = "reference"
os.makedirs(out_dir, exist_ok=True)
images_dir = os.path.join(out_dir, "images")
os.makedirs(images_dir, exist_ok=True)

print("Starting extraction...")
# write_images=True will extract images and save them. 
# image_path dictates where to save them.
md_text = pymupdf4llm.to_markdown(pdf_path, write_images=True, image_path=images_dir)

out_md = os.path.join(out_dir, "EntPhotons.md")
with open(out_md, "w", encoding="utf-8") as f:
    f.write(md_text)

print(f"Extraction complete. Saved to {out_md}")
