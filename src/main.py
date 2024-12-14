from textnode import *
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    '''dummy_textnode = TextNode("This is a TextNode", TextType.LINK, "https://www.example.com")
    print(dummy_textnode)'''

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

main()