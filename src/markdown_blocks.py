from textnode import text_node_to_html_node
from htmlnode import ParentNode
from inline_markdown import text_to_textnodes


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(block):
    if isheading(block):
        return "heading"
    if iscodeblock(block):
        return "code"
    if isquoteblock(block):
        return "quote"
    if isunordered(block):
        return "unordered_list"
   
    if isordered(block):
        return "ordered_list"
    return "paragraph"

def isheading(block):
    return block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### "))

def iscodeblock(block):
    return block.startswith("```") and block.endswith("```")

def isquoteblock(block):
    lines = block.split("\n")
    for line in lines:
        if not line.startswith(">"):
            return False
    return True

def isunordered(block):
    lines = block.split("\n")
    for line in lines:
        if not (line.startswith("* ") or line.startswith("- ")):
            return False
    return True

def isordered(block):
    lines = block.split("\n")
    for i in range(len(lines)):
        if not lines[i].startswith(str(i+1) + ". "):
            return False
    return True

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children)
        
def block_to_html_node(block):
    match block_to_block_type(block):
        case "heading":
            return heading_to_html_node(block)
        case "code":
            return code_to_html_node(block)
        case "quote":
            return quote_to_html_node(block)
        case "unordered_list":
            return unordered_to_html_node(block)
        case "ordered_list":
            return ordered_to_html_node(block)
        case "paragraph":
            return paragraph_to_html_node(block)
        case _:
            raise ValueError("Invalid block type")
            
def heading_to_html_node(block):
    sections = block.split(" ", 1)
    heading_type = str(sections[0].count("#"))
    block_text = sections[1]
    return ParentNode(f"h{heading_type}", text_to_children(block_text))

def code_to_html_node(block):
    text = block[3:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])

def quote_to_html_node(block):
    quote_list = []
    lines = block.split("\n")
    for line in lines:
        quote_list.append(line.lstrip(">").strip())
    quote = " ".join(quote_list)
    return ParentNode("blockquote", text_to_children(quote))

def unordered_to_html_node(block):
    lines = block.split("\n")
    line_items = lines_to_list_items(lines)
    return ParentNode("ul", line_items)

def ordered_to_html_node(block):
    lines = block.split("\n")
    line_items = lines_to_list_items(lines)
    return ParentNode("ol", line_items)

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    return ParentNode("p", text_to_children(paragraph))

def text_to_children(text):
    children = []
    nodes = text_to_textnodes(text)
    for node in nodes:
        children.append(text_node_to_html_node(node))
    return children

def lines_to_list_items(lines):
    html_list = []
    for line in lines:
        item = line.split(" ", 1)[1]
        html_list.append(ParentNode("li", text_to_children(item)))
    return html_list
