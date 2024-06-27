import re
import requests
from deep_translator import GoogleTranslator

class Content:
    def __init__(self, text: str, font_type, color: str, font_size, styling):
        self.text = text.replace("\n", "")
        self.font_type = font_type
        self.font_size = font_size
        self.styling = styling
        self.color = color
    
    def __append__(self, text: str):
        self.text += text
        
    def is_append(self, text, font_type, color: str, font_size, styling):
        style_difference =  abs(self.font_size - font_size)
        if (self.font_type == font_type) and (self.color == color) and (not bool(re.search(r'\w', text)) or style_difference < 1) and (self.styling == styling):
            return True
        return False

    def render(self):
        return {
            "text": self.text,
            "font_type": self.font_type,
            "font_size": self.font_size,
            "styling": self.styling,
            "color": self.color
        }

class Paragraph:
    def __init__(self, contents: list[Content]):
        self.contents = contents
        self.translated_text = ""
        
    def render(self):
        return [content.render() for content in self.contents]
    
    def get_text(self):
        return "".join([content.text for content in self.contents])
    
    def translate(self):
        text = self.get_text()
        self.translated_text = GoogleTranslator(source='auto', target='en').translate(text)
    
    def get_translate(self):
        return self.translated_text
    

class Page:
    def __init__(self, paragraphs: list[Paragraph], page_number: int):
        self.page_number = page_number
        self.paragraphs = paragraphs
        
    def render(self):
        return {
            "page_number": self.page_number,
            "paragraphs": [paragraph.render() for paragraph in self.paragraphs]
        }
        
class File:
    def __init__(self, file_name: str, pages: list[Page]) -> None:
        self.file_name = file_name
        self.pages = pages
    def render(self):
        return {
            "file_name": self.file_name,
            "pages": [page.render() for page in self.pages]
        }
        
    def translate(self):
        for page in self.pages:
            for paragraph in page.paragraphs:
                paragraph.translate()
    
    