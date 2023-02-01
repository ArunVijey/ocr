import PyPDF2
import pytesseract
from PIL import Image

# Open the PDF file
with open('document.pdf', 'rb') as file:
    pdf = PyPDF2.PdfFileReader(file)
    
    # Iterate through each page
    for page in range(pdf.numPages):
        # Extract the text from the page
        text = pdf.getPage(page).extractText()
        
        # Use Tesseract to convert the text into a format that can be read by the program
        text = pytesseract.image_to_string(Image.fromarray(text))
        
        # Print the extracted text
        print(text)
