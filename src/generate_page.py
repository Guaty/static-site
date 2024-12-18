import os
from pathlib import Path
from markdown_blocks import markdown_to_html_node, extract_title

    
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    content_list = os.listdir(dir_path_content)

    for path in content_list:
        src_path = os.path.join(dir_path_content, path)
        dest_path = os.path.join(dest_dir_path, path)

        if os.path.isfile(src_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(src_path, template_path, dest_path)
        elif os.path.isdir(src_path):
            generate_pages_recursive(src_path, template_path, dest_path)

def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")

    markdown_file = open(from_path, "r")
    markdown = markdown_file.read()
    markdown_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    new_page = template.replace("{{ Title }}", title).replace("{{ Content }}", content)

    dest_dirname = os.path.dirname(dest_path)
    if dest_dirname!= "":
        os.makedirs(dest_dirname, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(new_page)
   