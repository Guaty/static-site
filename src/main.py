import os
import shutil

from copystatic import copy_dir
from generate_page import generate_pages_recursive


path_static = "./static"
path_public = "./public"
path_markdown = "./content"
path_template = "./template.html"

def main():
    print("Deleting public directory...")
    if os.path.exists(path_public):
        shutil.rmtree(path_public)

    print("Copying static files to public directory...")
    copy_dir(path_static, path_public)

    print("Generating page...")
    generate_pages_recursive(path_markdown, path_template, path_public)

main()