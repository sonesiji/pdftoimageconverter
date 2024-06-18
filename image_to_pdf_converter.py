import cv2
import os
from fpdf import FPDF

# Function to read an image and convert it to a grayscale image
def process_image(image_path):
    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Image at {image_path} cannot be loaded.")
    
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    return gray_image

# Function to convert images to a PDF
def images_to_pdf(image_paths, pdf_path):
    pdf = FPDF()
    
    for image_path in image_paths:
        # Process the image
        processed_image = process_image(image_path)
        
        # Save the processed image temporarily
        temp_image_path = "temp_image.jpg"
        cv2.imwrite(temp_image_path, processed_image)
        
        # Add image to PDF
        pdf.add_page()
        pdf.image(temp_image_path, x=10, y=10, w=190)
        
        # Remove the temporary image file
        os.remove(temp_image_path)
    
    # Save the PDF to the specified path
    pdf.output(pdf_path)

# Main function
def main():
    # List of image paths
    image_paths = ["image1.png", "image2.png", "image3.png"]  # Replace with your image file names or paths
    
    # Output PDF path
    pdf_path = "output.pdf"  # Specify the output PDF file name
    
    # Convert images to PDF
    images_to_pdf(image_paths, pdf_path)
    print(f"PDF saved at {pdf_path}")

if __name__ == "__main__":
    main()
