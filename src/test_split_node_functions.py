import unittest
from split_node_functions import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

class  TestSplitNodesFunctions(unittest.TestCase):
    # SPLIT_NODES_DELIMITER FUNCTION TESTS
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

    # SPLIT_NODES_IMAGES FUNCTION TEST
    def test_split_image_just_text_type(self):
        nodes = [
            TextNode("This is just a test", TextType.TEXT)
        ]

        self.assertEqual(
            split_nodes_image(nodes),
            [TextNode("This is just a test", TextType.TEXT)]
        )

    def test_split_image_empty_text_value(self):
        nodes = [
            TextNode("", TextType.TEXT)
        ]

        self.assertEqual(
            split_nodes_image(nodes),
            []
        )

    def test_split_image_one_markdown_begin(self):
        nodes = [
            TextNode("![rick roll](https://i.imgur.com/aKaOqIh.gif) test", TextType.TEXT)
        ]

        self.assertEqual(
            split_nodes_image(nodes),
            [TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
             TextNode(" test", TextType.TEXT, None)]
        )

    def test_split_image_one_markdown_middle(self):
        nodes = [
            TextNode("text ![rick roll](https://i.imgur.com/aKaOqIh.gif) test", TextType.TEXT)
        ]

        self.assertEqual(
            split_nodes_image(nodes),
            [
                TextNode("text ", TextType.TEXT, None),
                TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
                TextNode(" test", TextType.TEXT, None)
            ]
        )

    def test_split_image_one_markdown_end(self):
        nodes = [
            TextNode("text ![rick roll](https://i.imgur.com/aKaOqIh.gif)", TextType.TEXT)
        ]

        self.assertEqual(
            split_nodes_image(nodes),
            [
                TextNode("text ", TextType.TEXT, None),
                TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif")
            ]
        )

    def test_split_image_one_markdown_mult_nodes(self):
        nodes = [
            TextNode("text ![rick roll](https://i.imgur.com/aKaOqIh.gif)", TextType.TEXT),
            TextNode("![rick roll](https://i.imgur.com/aKaOqIh.gif) test", TextType.TEXT)
        ]

        self.assertEqual(
            split_nodes_image(nodes),
            [
                TextNode("text ", TextType.TEXT, None),
                TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
                TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
                TextNode(" test", TextType.TEXT, None)
            ]
        )

    def test_split_image_two_markdown_begin(self):
        nodes = [
            TextNode("![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.TEXT)
        ]

        self.assertEqual(
            split_nodes_image(nodes),
            [
                TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
                TextNode(" and ", TextType.TEXT, None),
                TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg")
            ]
        )

    def test_split_image_two_markdown_wrapped(self):
        nodes = [
            TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg) test", TextType.TEXT)
        ]

        self.assertEqual(
            split_nodes_image(nodes),
            [
                TextNode("This is text with a ", TextType.TEXT, None),
                TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
                TextNode(" and ", TextType.TEXT, None),
                TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" test", TextType.TEXT)
            ]
        )

    def test_split_image_one_and_two_markdown_mult_nodes(self):
        nodes = [
            TextNode("text ![rick roll](https://i.imgur.com/aKaOqIh.gif)", TextType.TEXT),
            TextNode("![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.TEXT)
        ]

        self.assertEqual(
            split_nodes_image(nodes),
            [
                TextNode("text ", TextType.TEXT),
                TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
                TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
                TextNode(" and ", TextType.TEXT, None),
                TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg")
            ]
        )

    def test_split_image_two_and_two_markdown_mult_nodes(self):
        nodes = [
            TextNode("![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.TEXT),
            TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg) test", TextType.TEXT)
        ]

        self.assertEqual(
            split_nodes_image(nodes),
            [
                TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
                TextNode(" and ", TextType.TEXT, None),
                TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode("This is text with a ", TextType.TEXT, None),
                TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
                TextNode(" and ", TextType.TEXT, None),
                TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" test", TextType.TEXT)
            ]
        )

    # SPLIT_NODES_LINKS FUNCTION TEST
    def test_split_link_just_text_type(self):
        nodes = [
            TextNode("This is just a test", TextType.TEXT)
        ]

        self.assertEqual(
            split_nodes_link(nodes),
            [TextNode("This is just a test", TextType.TEXT)]
        )

    def test_split_link_empty_text_value(self):
        nodes = [
            TextNode("", TextType.TEXT)
        ]

        self.assertEqual(
            split_nodes_link(nodes),
            []
        )

    def test_split_link_one_markdown_begin(self):
        nodes = [
            TextNode("[rick roll](https://i.imgur.com/aKaOqIh.gif) test", TextType.TEXT)
        ]

        self.assertEqual(
            split_nodes_link(nodes),
            [TextNode("rick roll", TextType.LINK, "https://i.imgur.com/aKaOqIh.gif"),
             TextNode(" test", TextType.TEXT, None)]
        )

    def test_split_link_one_markdown_middle(self):
        nodes = [
            TextNode("text [rick roll](https://i.imgur.com/aKaOqIh.gif) test", TextType.TEXT)
        ]

        self.assertEqual(
            split_nodes_link(nodes),
            [
                TextNode("text ", TextType.TEXT, None),
                TextNode("rick roll", TextType.LINK, "https://i.imgur.com/aKaOqIh.gif"),
                TextNode(" test", TextType.TEXT, None)
            ]
        )

    def test_split_link_one_markdown_end(self):
        nodes = [
            TextNode("text [rick roll](https://i.imgur.com/aKaOqIh.gif)", TextType.TEXT)
        ]

        self.assertEqual(
            split_nodes_link(nodes),
            [
                TextNode("text ", TextType.TEXT, None),
                TextNode("rick roll", TextType.LINK, "https://i.imgur.com/aKaOqIh.gif")
            ]
        )

    def test_split_image_one_markdown_mult_nodes(self):
        nodes = [
            TextNode("text [rick roll](https://i.imgur.com/aKaOqIh.gif)", TextType.TEXT),
            TextNode("[rick roll](https://i.imgur.com/aKaOqIh.gif) test", TextType.TEXT)
        ]

        self.assertEqual(
            split_nodes_link(nodes),
            [
                TextNode("text ", TextType.TEXT, None),
                TextNode("rick roll", TextType.LINK, "https://i.imgur.com/aKaOqIh.gif"),
                TextNode("rick roll", TextType.LINK, "https://i.imgur.com/aKaOqIh.gif"),
                TextNode(" test", TextType.TEXT, None)
            ]
        )

    def test_split_link_two_markdown_begin(self):
        nodes = [
            TextNode("[rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.TEXT)
        ]

        self.assertEqual(
            split_nodes_link(nodes),
            [
                TextNode("rick roll", TextType.LINK, "https://i.imgur.com/aKaOqIh.gif"),
                TextNode(" and ", TextType.TEXT, None),
                TextNode("obi wan", TextType.LINK, "https://i.imgur.com/fJRm4Vk.jpeg")
            ]
        )

    def test_split_link_two_markdown_wrapped(self):
        nodes = [
            TextNode("This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg) test", TextType.TEXT)
        ]

        self.assertEqual(
            split_nodes_link(nodes),
            [
                TextNode("This is text with a ", TextType.TEXT, None),
                TextNode("rick roll", TextType.LINK, "https://i.imgur.com/aKaOqIh.gif"),
                TextNode(" and ", TextType.TEXT, None),
                TextNode("obi wan", TextType.LINK, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" test", TextType.TEXT)
            ]
        )

    def test_split_link_one_and_two_markdown_mult_nodes(self):
        nodes = [
            TextNode("text [rick roll](https://i.imgur.com/aKaOqIh.gif)", TextType.TEXT),
            TextNode("[rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.TEXT)
        ]

        self.assertEqual(
            split_nodes_link(nodes),
            [
                TextNode("text ", TextType.TEXT),
                TextNode("rick roll", TextType.LINK, "https://i.imgur.com/aKaOqIh.gif"),
                TextNode("rick roll", TextType.LINK, "https://i.imgur.com/aKaOqIh.gif"),
                TextNode(" and ", TextType.TEXT, None),
                TextNode("obi wan", TextType.LINK, "https://i.imgur.com/fJRm4Vk.jpeg")
            ]
        )

    def test_split_link_two_and_two_markdown_mult_nodes(self):
        nodes = [
            TextNode("[rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.TEXT),
            TextNode("This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg) test", TextType.TEXT)
        ]

        self.assertEqual(
            split_nodes_link(nodes),
            [
                TextNode("rick roll", TextType.LINK, "https://i.imgur.com/aKaOqIh.gif"),
                TextNode(" and ", TextType.TEXT, None),
                TextNode("obi wan", TextType.LINK, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode("This is text with a ", TextType.TEXT, None),
                TextNode("rick roll", TextType.LINK, "https://i.imgur.com/aKaOqIh.gif"),
                TextNode(" and ", TextType.TEXT, None),
                TextNode("obi wan", TextType.LINK, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" test", TextType.TEXT)
            ]
        )