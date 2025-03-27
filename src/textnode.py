from enum import Enum

class TextType(Enum):    
    normal_text = "Normal_text"
    bold = "**Bold text**"
    italic = "_Italic text_"
    code_text = "`Code text`"
    link = "[anchor text](url)"
    image = "![alt text](url)"

class TextNode():
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        if (self.text == other.text
        and self.text_type == other.text_type
        and self.url == other.url):
            return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
