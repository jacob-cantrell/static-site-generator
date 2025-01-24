import re

def extract_markdown_images(text):
    images = []
    # Find all markdown images in text
    images_found = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

    # Check if anything was found; if not, return empty list - otherwise return found
    if images_found is None:
        return images

    return images_found

def extract_markdown_link(text):
    links = []
    # Find all markdown links in text
    links_found = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

    # Check if anything was found; if not, return empty list - otherwise return found
    if links_found is None:
        return links

    return links_found