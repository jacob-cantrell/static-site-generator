import re

def extract_markdown_images(text):
    # Find all markdown images in text
    images_found = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

    # Check if anything was found; if not, return empty list - otherwise return found
    if images_found is None:
        return None

    return images_found

def extract_markdown_link(text):
    # Find all markdown links in text
    links_found = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

    # Check if anything was found; if not, return empty list - otherwise return found
    if links_found is None:
        return None

    return links_found