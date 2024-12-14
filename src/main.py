from textnode import *
from htmlnode import *

def main():
    
    dummy_textnode = TextNode("This is a TextNode", TextType.LINK, "https://www.example.com")
    dummy_leafnode = text_node_to_html_node(dummy_textnode)

    image_textnode = TextNode("This should be an image", TextType.IMAGE, "/src/img/test.jpg")
    image_leafnode = text_node_to_html_node(image_textnode)
    
    print(dummy_leafnode.to_html())
    print(image_leafnode.to_html())
    

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


main()