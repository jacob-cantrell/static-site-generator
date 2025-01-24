import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        node = HTMLNode("test tag", "test value", ["test", "test2"], {"a": "href", "color": "white"})
        try:
            node.to_html()
        except NotImplementedError:
            self.assertRaises(NotImplementedError)

    def test_props_to_html(self):
        node = HTMLNode("test tag", "test value", ["test", "test2"], {"a": "href", "color": "white"})
        self.assertEqual(node.props_to_html(), " a=\"href\" color=\"white\"")

    def test_props_to_html_has_leading_space(self):
        node = HTMLNode("test tag", "test value", ["test", "test2"], {"a": "href", "color": "white"})
        self.assertNotEqual(node.props_to_html(), "a=\"href\" color=\"white\"")