import unittest
from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class  TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_node_asterik_delimiter(self):
        nodes = [
            TextNode("test *test text* test 2", TextType.TEXT)
        ]

        new_nodes = split_nodes_delimiter(nodes, "*", TextType.BOLD)

        self.assertEqual(
            new_nodes,
            [
                TextNode("test ", TextType.TEXT),
                TextNode("test text", TextType.BOLD),
                TextNode(" test 2", TextType.TEXT)
            ]
        )

    def test_split_node_double_asterik_delimiter(self):
        nodes = [
            TextNode("test **test text** test 2", TextType.TEXT)
        ]

        new_nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)

        self.assertEqual(
            new_nodes,
            [
                TextNode("test ", TextType.TEXT),
                TextNode("test text", TextType.BOLD),
                TextNode(" test 2", TextType.TEXT)
            ]
        )

    def test_split_node_back_quote_delimiter(self):
        nodes = [
            TextNode("test `test text` test 2", TextType.TEXT)
        ]

        new_nodes = split_nodes_delimiter(nodes, "`", TextType.BOLD)

        self.assertEqual(
            new_nodes,
            [
                TextNode("test ", TextType.TEXT),
                TextNode("test text", TextType.BOLD),
                TextNode(" test 2", TextType.TEXT)
            ]
        )

    def test_split_multiple_nodes_w_delimiter(self):
        nodes = [
            TextNode("test *test text* test 2", TextType.TEXT),
            TextNode("second *test* text", TextType.TEXT)
        ]

        new_nodes = split_nodes_delimiter(nodes, "*", TextType.BOLD)

        self.assertEqual(
            new_nodes,
            [
                TextNode("test ", TextType.TEXT),
                TextNode("test text", TextType.BOLD),
                TextNode(" test 2", TextType.TEXT),
                TextNode("second ", TextType.TEXT),
                TextNode("test", TextType.BOLD),
                TextNode(" text", TextType.TEXT)
            ]
        )

    def test_split_node_no_closing_delimiter(self):
        nodes = [
            TextNode("test `test text test 2", TextType.TEXT)
        ]

        try:
            split_nodes_delimiter(nodes, "`", TextType.BOLD)
        except Exception:
            self.assertRaises(Exception)

    def test_split_node_beginning_of_text(self):
        nodes = [
            TextNode("`test `text", TextType.TEXT)
        ]

        new_nodes = split_nodes_delimiter(nodes, "`", TextType.BOLD)

        self.assertEqual(
            new_nodes,
            [
                TextNode("test ", TextType.BOLD),
                TextNode("text", TextType.TEXT)
            ]
        )

    def test_split_node_end_of_text(self):
        nodes = [
            TextNode("test `text`", TextType.TEXT)
        ]

        new_nodes = split_nodes_delimiter(nodes, "`", TextType.BOLD)

        self.assertEqual(
            new_nodes,
            [
                TextNode("test ", TextType.TEXT),
                TextNode("text", TextType.BOLD)
            ]
        )

    def test_split_nodes_not_text_type(self):
        nodes = [
            TextNode("test `text`", TextType.BOLD)
        ]

        new_nodes = split_nodes_delimiter(nodes, "`", TextType.BOLD)

        self.assertEqual(
            new_nodes,
            [
                TextNode("test `text`", TextType.BOLD)
            ]
        )