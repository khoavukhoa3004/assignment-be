
import pymupdf
import os 
import fitz

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
    
# Question 2
# def extract_paragraph_text(file_path: str, target_folder: str):
#     doc = pymupdf.open(file_path)
#     if not os.path.exists(target_folder):
#         os.makedirs(target_folder)
    
#     out = open(f'{target_folder}/text.txt', "wb")
#     for page_idx, page in enumerate(doc, start=1):
#         print("page...", page)
#         paragraphs = page.get_text("blocks")
#         lines = page.get_text("html")
#         for item in paragraphs:
#             # print(item)
#             # print(".....")
#             # text = item[4].replace('\n', '').encode("utf8")
#             # out.write(text)
#             # # out.write(bytes((12,)))
#             # out.write('\n'.encode('utf-8'))    
#             print(item) 
#             if item[4] == 0:  # Check if the block is a paragraph
#                 paragraph_style = {
#                     "font": item[2],
#                     "font_size": item[3],
#                     "color": item[5],
#                     "alignment": item[6],
#                     "line_height": item[7],
#                     "line_width": item[8],
#                     "line_spacing": item[9],
#                 }
#                 print(paragraph_style)
#                 # paragraph_styles.append(paragraph_style)
 
#         # for line in page.get_text("html").splitlines():
#         #     print(line)
#     out.close()

