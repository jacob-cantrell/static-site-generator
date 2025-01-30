from os import path, listdir, mkdir
from shutil import copy, rmtree

def copy_file_to_public(source_path, dest_path, item):
    # If a file, add to public based on path
    if path.isfile(path.join(source_path, item)):
        copy(path.join(source_path, item), path.join(dest_path, item))
    # Otherwise, it's a directory - loop through and recursively call on each file
    else:
        # Update new paths to add directory
        new_source_path = path.join(source_path, item)
        new_dest_path = path.join(dest_path, item)
        # Make directory - loop through directory and call function
        mkdir(new_dest_path)
        items = listdir(new_source_path)
        for obj in items:
            copy_file_to_public(new_source_path, new_dest_path, obj)

def copy_static_to_public():
    # If public directory exists, remove and recreate to empty directory
    if path.exists("public/"):
        rmtree("public/")
        mkdir("public")

    # Get list of directory items
    static_items = listdir("static/")
    for item in static_items:
        copy_file_to_public("static/", "public/", item)