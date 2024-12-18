import unittest
from markdown_blocks import markdown_to_blocks, block_to_block_type


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

if __name__ == "__main__":
    unittest.main()