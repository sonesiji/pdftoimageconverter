import cv2
import os
from fpdf import FPDF

def process_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Image at {image_path} cannot be loaded.")
    
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image

def images_to_pdf(image_paths, pdf_path):
    pdf = FPDF()
    
    for image_path in image_paths:
        processed_image = process_image(image_path)
        temp_image_path = "temp_image.jpg"
        cv2.imwrite(temp_image_path, processed_image)
        
        pdf.add_page()
        pdf.image(temp_image_path, x=10, y=10, w=190)
        
        os.remove(temp_image_path)
    
    pdf.output(pdf_path)
