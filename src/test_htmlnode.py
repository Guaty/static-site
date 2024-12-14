import unittest
from htmlnode import HTMLNode, LeafNode


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
            "HTMLNode(None, I got no value, children: None, None)"            
        )

if __name__ == "__main__":
    unittest.main()