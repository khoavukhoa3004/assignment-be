
import json
import io
import pymupdf
import os 
import fitz
from paragraph import Content, Paragraph, Page, File

def get_pdf_document(file_path):
    # Check if the file is a PDF
    try:
        pdf_doc = fitz.open(file_path)
        if pdf_doc.is_pdf:
            return pdf_doc
        else:
            converted_pdf = pdf_doc.convert_to_pdf()
            return fitz.open("pdf", converted_pdf)
    
    except fitz.errors.FileDataError:
        pass


# Question 1
def extract_document(file_path: str, target_folder: str):
    doc = pymupdf.open(file_path)
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
        
    out = open(f'{target_folder}/text.txt', "wb")
    for page_idx, page in enumerate(doc, start=1):
        text = page.get_text().encode("utf8")
        out.write(text)    
        out.write(bytes((12,))) # write page delimiter (form feed 0x0C)
        
        image_list = page.get_images()
        if not os.path.exists(f'{target_folder}/images/{page_idx}'):
            os.makedirs(f'{target_folder}/images/{page_idx}')
        for idx, img in enumerate(image_list, start=1):
            xref = img[0] # get the XREF of the image
            pix = pymupdf.Pixmap(doc, xref) # create a Pixmap

            if pix.n - pix.alpha > 3: # CMYK: convert to RGB first
                pix = pymupdf.Pixmap(pymupdf.csRGB, pix)

            pix.save(f'{target_folder}/images/{page_idx}/{idx}.png') # save the image as png
            pix = None
    out.close()

def extract_paragraph_text(file_path: str, target_folder: str):
    doc = get_pdf_document(file_path)
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    
    rendered_file = File(file_path, [])
    
    for page_idx, page in enumerate(doc, start=1):
        redered_page = Page([], page_idx)
        dict = page.get_text("dict")
        blocks = dict["blocks"]
        for block in blocks:
            paragraph = Paragraph([])
            if "lines" in block.keys() and block['lines'].__len__() > 0:
                spans = block['lines']
                for span in spans:
                    data = span['spans']
                    for lines in data:
                        if lines['text'].strip():
                            if len(paragraph.contents) > 0 and paragraph.contents[-1].is_append(lines['text'], lines['font'], lines['color'], lines['size'], lines['flags']):
                                paragraph.contents[-1].__append__(lines['text'])
                            else:
                                content = Content(lines['text'], lines['font'], lines['color'], lines['size'], lines['flags'])
                                paragraph.contents.append(content)
            if paragraph.contents.__len__() > 0:
                redered_page.paragraphs.append(paragraph) 
        rendered_file.pages.append(redered_page)                       
    with open(f'{target_folder}/text.json', 'w') as out:
        json.dump(rendered_file.render(), out, indent=4)
        