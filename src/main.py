from textnode import *
from htmlnode import *
from inline_markdown import *
from markdown_blocks import markdown_to_blocks

def main():
    
    doc = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
    block_list = markdown_to_blocks(doc)
    print(block_list)

main()