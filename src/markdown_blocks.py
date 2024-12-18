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
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return True
    return False

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