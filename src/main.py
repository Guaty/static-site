from textnode import *
from htmlnode import HTMLNode, LeafNode

def main():
    '''dummy_textnode = TextNode("This is a TextNode", TextType.LINK, "https://www.example.com")
    print(dummy_textnode)'''

    dummy_htmlnode = LeafNode(None, "I got no value")
    print(dummy_htmlnode)

main()