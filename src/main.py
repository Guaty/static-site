from textnode import *
from htmlnode import *
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links

def main():
    '''
    dummy_textnode = TextNode("This is a TextNode", TextType.LINK, "https://www.example.com")
    dummy_leafnode = text_node_to_html_node(dummy_textnode)

    image_textnode = TextNode("This should be an image", TextType.IMAGE, "/src/img/test.jpg")
    image_leafnode = text_node_to_html_node(image_textnode)
    
    print(dummy_leafnode.to_html())
    print(image_leafnode.to_html())

    split_node = TextNode("I **AM** THE **MAN**", TextType.TEXT)
    print(split_node)
    new_nodes = split_nodes_delimiter([split_node], "**", TextType.BOLD)
    print(new_nodes)
    '''
    

    '''
    dummy_htmlnode = ParentNode(
        "a", 
         [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ]
    )
    print(dummy_htmlnode.to_html())
    '''
    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    regex_list = extract_markdown_links(text)
    print(regex_list)

    invalid_link = "This [link](nada) is invalid"
    invalid_list = extract_markdown_links(invalid_link)
    print(invalid_list)


main()