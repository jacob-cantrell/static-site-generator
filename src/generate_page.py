from block_functions import markdown_to_html_node
from os import path, makedirs, listdir
from pathlib import Path

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line.strip("# ")
            
    raise Exception("No h1 header found!")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    # Define variables for markdown file and template file
    markdown = ""
    template = ""
    new_html = ""

    # Read from markdown and templates and close files
    from_file = open(from_path)
    markdown = from_file.read()
    from_file.close()

    template_file = open(template_path)
    template = template_file.read()
    template_file.close()

    # Convert markdown to HTML string and extract title
    html_str = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    # Replace placeholders with title and content
    new_html = template.replace("{{ Title }}", title)
    new_html = new_html.replace("{{ Content }}", html_str)

    # Create necessary directories for the destination file path
    directory = path.dirname(dest_path)
    makedirs(directory, exist_ok=True)

    # Write full HTML page (new_html) to dest_path
    file = open(dest_path, 'w')
    file.write(new_html)
    file.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    # Get file list of content directory
    file_list = listdir(dir_path_content)

    # Traverse files and check if file or directory
    for file in file_list:
        # If it's a file, then check if it's markdown
        if path.isfile(path.join(dir_path_content, file)):
            if file.endswith(".md"):
                end_file = file.replace(".md", ".html")
                generate_page(path.join(dir_path_content, file), template_path, path.join(dest_dir_path, end_file))
        else: # directory
            generate_pages_recursive(path.join(dir_path_content, file), template_path, path.join(dest_dir_path, file))