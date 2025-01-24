import re

def extract_markdown_images(text):
    # Find all markdown images in text (returns empty list if nothing found)
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_link(text):
    # Find all markdown links in text (returns empty list if nothing found)
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)