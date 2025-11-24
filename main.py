import gradio as gr
from PIL import Image

def image_to_pdf(image_paths):
    #load images from file paths, convert them to RGB format
    image_list=[Image.open(image).convert("RGB") for image in image_paths]

    #save images as a single pdf file
    pdf_path="merged_images.pdf"
    image_list[0].save(pdf_path, save_all=True, append_images=image_list[1:])

    return pdf_path

interface = gr.Interface(
    fn=image_to_pdf,
    inputs=gr.Files(type="filepath", file_types=[".png", ".jpg", ".jpeg"]),
    outputs=gr.File(label="Download Merged PDF"),   
    title="Multiple Images to PDF Converter",
    description="Upload multiple images to merge them into a single PDF file."
)

interface.launch(share=True )



