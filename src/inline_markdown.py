import re

from textnode import *

def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    nodes = split_nodes_images((split_nodes_links([node])))
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    return nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        #interested only in raw text TextNodes
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        #check if the delimiters "close" the formatted section
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            #in case the text begins or ends with delimiter
            if sections[i] == "":
                continue
            #all 'even' sections would be outside formatted delimiters, so those remain text
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            #all 'odd' sections would be inside formatted delimiters, so those are converted
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def split_nodes_images(old_nodes):
    new_nodes = []
    for node in old_nodes:
        split_nodes = []
        remaining_text = node.text
        extracted_images = extract_markdown_images(remaining_text)
        if extracted_images == []:
            new_nodes.append(node)
            continue
        for image in extracted_images:
            image_alt, image_url = image
            #splitting to before and after image
            sections = remaining_text.split(f"![{image_alt}]({image_url})", 1) 
            
            #processing the text before the image, making sure there's something to process
            if len(sections[0]) > 0:
                split_nodes.append(TextNode(sections[0], TextType.TEXT))
            #processing the image itself
            split_nodes.append(TextNode(image_alt, TextType.IMAGE, image_url))
            #passing the remaining text to be processed in the next iteration
            remaining_text = sections[1]
        if len(remaining_text) > 0:
            split_nodes.append(TextNode(remaining_text, TextType.TEXT))   
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_links(old_nodes):
    new_nodes = []
    for node in old_nodes:
        split_nodes = []
        remaining_text = node.text
        extracted_links = extract_markdown_links(remaining_text)
        if extracted_links == []:
            new_nodes.append(node)
            continue
        for link in extracted_links:
            anchor_text, link_url = link
            sections = remaining_text.split(f"[{anchor_text}]({link_url})", 1)
            
            #processing the text before the link, making sure there's something to process
            if len(sections[0]) > 0:
                split_nodes.append(TextNode(sections[0], TextType.TEXT))
            #processing the link itself
            split_nodes.append(TextNode(anchor_text, TextType.LINK, link_url))
            #passing the remaining text to be processed in the next iteration
            remaining_text = sections[1]
        if len(remaining_text) > 0:
            split_nodes.append(TextNode(remaining_text, TextType.TEXT))            
        new_nodes.extend(split_nodes)
    return new_nodes


