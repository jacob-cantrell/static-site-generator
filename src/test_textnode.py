import unittest
from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    # Test Node Equality
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq_diff_text(self):
        node = TextNode("This is a text note", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_not_eq_diff_text_type(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_with_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://google.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://google.com")
        self.assertEqual(node, node2)

    def test_not_eq_with_diff_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://google.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://boot.dev")
        self.assertNotEqual(node, node2)

    # Test text_node_to_leaf_node
    def test_normal(self):
        node = TextNode("test text", TextType.TEXT)
        leaf = text_node_to_html_node(node)
        self.assertEqual(
            leaf.to_html(),
            "test text"
        )

    def test_bold(self):
        node = TextNode("test text", TextType.BOLD)
        leaf = text_node_to_html_node(node)
        self.assertEqual(
            leaf.to_html(),
            "<b>test text</b>"
        )

    def test_italics(self):
        node = TextNode("test text", TextType.ITALIC)
        leaf = text_node_to_html_node(node)
        self.assertEqual(
            leaf.to_html(),
            "<i>test text</i>"
        )

    def test_code(self):
        node = TextNode("test text", TextType.CODE)
        leaf = text_node_to_html_node(node)
        self.assertEqual(
            leaf.to_html(),
            "<code>test text</code>"
        )

    def test_link(self):
        node = TextNode("test text", TextType.LINK, "https://google.com")
        leaf = text_node_to_html_node(node)
        self.assertEqual(
            leaf.to_html(),
            "<a href=\"https://google.com\">test text</a>"
        )

    def test_image(self):
        node = TextNode("test text", TextType.IMAGE, "https://google.com")
        leaf = text_node_to_html_node(node)
        self.assertEqual(
            leaf.to_html(),
            "<img src=\"https://google.com\" alt=\"test text\"></img>"
        )

    def test_invalid_type(self):
        node = TextNode("test text", None)
        try:
            text_node_to_html_node(node)
        except Exception:
            self.assertRaises(Exception)

if __name__ == "__main__":
    unittest.main()