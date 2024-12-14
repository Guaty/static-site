from textnode import *
from htmlnode import HTMLNode

def main():
    '''dummy_textnode = TextNode("This is a TextNode", TextType.LINK, "https://www.example.com")
    print(dummy_textnode)'''

    dummy_htmlnode = HTMLNode("p", "This is an HTMLNode", "blep", {"class": "blueberry"})
    print(dummy_htmlnode)

main()