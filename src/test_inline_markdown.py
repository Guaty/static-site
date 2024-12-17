import unittest
from inline_markdown import (
    split_nodes_delimiter, 
    extract_markdown_links,
    extract_markdown_images,
    split_nodes_images,
    split_nodes_links,
    text_to_textnodes
)

from textnode import TextNode, TextType


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_invalid_markdown(self):
        node = TextNode("This is an *invalid format", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "*", TextType.ITALIC)

    def test_link_extraction(self):
        text = "I have a [link](https://www.example.com)"
        self.assertListEqual(
            [("link", "https://www.example.com")],
            extract_markdown_links(text)
        )

    def test_multi_link_extraction(self):
        text = "[link1](https://www.google.com/) and [link2](https://www.boot.dev/)"
        self.assertListEqual(
            [
                ("link1", "https://www.google.com/"),
                ("link2", "https://www.boot.dev/")
            ],
            extract_markdown_links(text)
        )

    def test_image_extraction(self):
        pic = "I'm a ![pretty image](src/img/pretty_image.jpg)"
        self.assertListEqual(
            [("pretty image", "src/img/pretty_image.jpg")],
            extract_markdown_images(pic)
        )

    def test_delim_link(self):
        node = TextNode("This is text with an [example link](https://www.example.com).", TextType.TEXT)
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("example link", TextType.LINK, "https://www.example.com"),
                TextNode(".", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_image(self):
        node = TextNode("I'm a ![pretty image](src/img/pretty_image.jpg)!", TextType.TEXT)
        new_nodes = split_nodes_images([node])
        self.assertListEqual(
            [
                TextNode("I'm a ", TextType.TEXT),
                TextNode("pretty image", TextType.IMAGE, "src/img/pretty_image.jpg"),
                TextNode("!", TextType.TEXT)
            ],
            new_nodes,
        )

    def test_delim_no_image(self):
        node = TextNode("I'm not an image", TextType.TEXT)
        new_nodes = split_nodes_images([node])
        self.assertListEqual([node], new_nodes)

    def test_delim_no_link(self):
        node = TextNode("I'm not a link", TextType.TEXT)
        new_nodes = split_nodes_images([node])
        self.assertListEqual([node], new_nodes)

    def test_delim_multi_link(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
            ],
            new_nodes,
        )

    def test_delim_multi_image(self):
        node = TextNode("This is text with ![picture one](src/images/picture_one.jpg) and ![picture two](src/images/picture_two.gif)", TextType.TEXT)
        new_nodes = split_nodes_images([node])
        self.assertListEqual(
            [
                TextNode("This is text with ", TextType.TEXT),
                TextNode("picture one", TextType.IMAGE, "src/images/picture_one.jpg"),
                TextNode(" and ", TextType.TEXT),
                TextNode("picture two", TextType.IMAGE, "src/images/picture_two.gif"),
            ],
            new_nodes,
        )

    def test_delim_link_and_image(self):
        node = TextNode("This is text with [a link](http://www.blep.com) and ![an image](src/img/test_image.pic)", TextType.TEXT)
        new_nodes = split_nodes_links([node])
        new_nodes = split_nodes_images(new_nodes)
        self.assertListEqual(
            [
                TextNode("This is text with ", TextType.TEXT),
                TextNode("a link", TextType.LINK, "http://www.blep.com"),
                TextNode(" and ", TextType.TEXT),
                TextNode("an image", TextType.IMAGE, "src/img/test_image.pic"),
            ],
            new_nodes,
        )
    
    def test_invalid_link_syntax(self):
        node = TextNode("Imma [broken link(nada.zilch)", TextType.TEXT)
        new_nodes = split_nodes_links([node])
        self.assertListEqual([node], new_nodes)

    def test_invalid_image_syntax(self):
        node =  TextNode("Imma ![broken pic(nada.zilch)", TextType.TEXT)
        new_nodes = split_nodes_images([node])
        self.assertListEqual([node], new_nodes)

    def test_link_at_start(self):
        node = TextNode("[Start](https://www.google.com) here", TextType.TEXT)
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
            [
                TextNode("Start", TextType.LINK, "https://www.google.com"),
                TextNode(" here", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_image_at_start(self):
        node = TextNode("![BAM!](src/images/BAM.gif) haha", TextType.TEXT)
        new_nodes = split_nodes_images([node])
        self.assertListEqual(
            [
                TextNode("BAM!", TextType.IMAGE, "src/images/BAM.gif"),
                TextNode(" haha", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_text_to_textnode(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            new_nodes
        )

if __name__ == "__main__":
    unittest.main()
