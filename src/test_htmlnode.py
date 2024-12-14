import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )
    
    def test_leaf(self):
        node = LeafNode(
            "a",
            "Click me!",
            {"href": "https://www.example.com"}
        )
        self.assertIn(
            "href",
            node.props
        )

    def test_leaf_has_no_children(self):
        node = LeafNode(
            "p",
            "I shouldn't have children. They suck.",
            {"id": "no-children"}
        )
        self.assertFalse(node.children)

    def test_to_html(self):
        node = LeafNode(
            "h1",
            "I AM HTML!!!!",
            {"class": "loud"}
        )
        self.assertEqual(
            node.to_html(),
            '<h1 class="loud">I AM HTML!!!!</h1>'
        )

    def test_leaf_repr(self):
        node = LeafNode(None, "I got no value")
        self.assertEqual(
            node.__repr__(),
            "LeafNode(None, I got no value, None)"            
        )

    def test_parent_html(self):
        node = ParentNode(
            "a", 
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]
        )
        self.assertEqual(
            node.to_html(),
            "<a><b>Bold text</b>Normal text<i>italic text</i>Normal text</a>"
        )

    def test_nested_parents(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("p", "I am a paragraph"),
                LeafNode("p", "So am I!", {"id": "partially-nested-paragraph"})
            ],
            {"class": "nested-header"}
        )

        super_node = ParentNode(
            "h1",
            [
                node,
                node,
                node
            ],
            {"class": "top-header"}
        )
        self.assertEqual(
            super_node.to_html(),
            '<h1 class="top-header"><h2 class="nested-header"><p>I am a paragraph</p><p id="partially-nested-paragraph">So am I!</p></h2><h2 class="nested-header"><p>I am a paragraph</p><p id="partially-nested-paragraph">So am I!</p></h2><h2 class="nested-header"><p>I am a paragraph</p><p id="partially-nested-paragraph">So am I!</p></h2></h1>'
        )

    def test_no_children(self):
        node = ParentNode(
            "h3",
            None,
            {"no": "way"}
        )
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()