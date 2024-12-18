import unittest
from markdown_blocks import *


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_block_to_blocktype_heading(self):
        block = "## This is a heading"
        self.assertEqual(block_to_block_type(block), "heading")

    def test_block_to_blocktype_code(self):
        block = "```This is a code block.```"
        self.assertEqual(block_to_block_type(block), "code")

    def test_block_to_blocktype_code_newlines(self):
        block = "```This is a code block.\nI got lots of code```"
        self.assertEqual(block_to_block_type(block), "code")

    def test_block_to_blocktype_quote(self):
        block = ">Quote\n>2nd quote\n>3rd quote"
        self.assertEqual(block_to_block_type(block), "quote")

    def test_block_to_blocktype_unordered(self):
        block = """* I'm a list\n* An unordered list\n* Just absolute chaos"""
        self.assertEqual(block_to_block_type(block), "unordered_list")

    def test_block_to_blocktype_ordered(self):
        block = """1. I'm an ordered list\n2. I'm item 2\n3. Closing with three"""
        self.assertEqual(block_to_block_type(block), "ordered_list")

    def test_block_to_blocktype_paragraph(self):
        block = "Just a paragraph"
        self.assertEqual(block_to_block_type(block), "paragraph")

    def test_block_to_blocktype_invalid_heading(self):
        block = "###No space here"
        self.assertEqual(block_to_block_type(block), "paragraph")

    def test_block_to_blocktype_inline_code(self):
        block = "This is a paragraph with `code` inline."
        self.assertEqual(block_to_block_type(block), "paragraph")

    def test_block_to_blocktype_mixed_content(self):
        block = "## Header with a list\n1. List item one\n2. List item two"
        self.assertEqual(block_to_block_type(block), "heading")
    
    def test_block_to_blocktype_empty_code_block(self):
        block = "```\n```"
        self.assertEqual(block_to_block_type(block), "code")

    def test_markdown_to_heading(self):
        markdown = "## I'm an h2 heading"
        node = markdown_to_html_node(markdown)
        self.assertEqual(node.to_html(), "<div><h2>I'm an h2 heading</h2></div>")

    def test_markdown_to_paragraph(self):
        markdown = "Just a paragraph with **bold** and *italicized* text."
        node = markdown_to_html_node(markdown)
        self.assertEqual(node.to_html(), "<div><p>Just a paragraph with <b>bold</b> and <i>italicized</i> text.</p></div>")

    def test_markdown_to_code(self):
        markdown = "```This is a small code block```"
        node = markdown_to_html_node(markdown)
        self.assertEqual(node.to_html(), "<div><pre><code>This is a small code block</code></pre></div>")

    def test_markdown_to_blockquote(self):
        markdown = ">Quote\n>2nd quote\n>3rd quote"
        node = markdown_to_html_node(markdown)
        self.assertEqual(node.to_html(), "<div><blockquote>Quote 2nd quote 3rd quote</blockquote></div>")

    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

    def test_extract_title(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""
        self.assertEqual("this is an h1", extract_title(md))

    def test_extract_tile_error(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        with self.assertRaises(Exception):
            extract_title(md)

if __name__ == "__main__":
    unittest.main()