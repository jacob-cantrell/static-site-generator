import unittest
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType

class TestTextToTextNode(unittest.TestCase):
    # TEST TEXT TO TEXTNODE
    def test_text_to_node_bold_only(self):
        text = "This text **just** has bold"

        self.assertEqual(
            text_to_textnodes(text),
            [
                TextNode("This text ", TextType.TEXT),
                TextNode("just", TextType.BOLD),
                TextNode(" has bold", TextType.TEXT)
            ]
        )

    def test_text_to_node_italic_only(self):
        text = "This text *just* has italic"

        self.assertEqual(
            text_to_textnodes(text),
            [
                TextNode("This text ", TextType.TEXT),
                TextNode("just", TextType.ITALIC),
                TextNode(" has italic", TextType.TEXT)
            ]
        )

    def test_text_to_node_code_only(self):
        text = "This text `just` has code"

        self.assertEqual(
            text_to_textnodes(text),
            [
                TextNode("This text ", TextType.TEXT),
                TextNode("just", TextType.CODE),
                TextNode(" has code", TextType.TEXT)
            ]
        )

    def test_text_to_node_image_only(self):
        text = "This text ![google](https://google.com) just has image"

        self.assertEqual(
            text_to_textnodes(text),
            [
                TextNode("This text ", TextType.TEXT),
                TextNode("google", TextType.IMAGE, "https://google.com"),
                TextNode(" just has image", TextType.TEXT)
            ]
        )

    def test_text_to_node_link_only(self):
        text = "This text [google](https://google.com) just has link"

        self.assertEqual(
            text_to_textnodes(text),
            [
                TextNode("This text ", TextType.TEXT),
                TextNode("google", TextType.LINK, "https://google.com"),
                TextNode(" just has link", TextType.TEXT)
            ]
        )

    def test_text_to_node_mult_bold_only(self):
        text = "This text has **bold** and **bold2**"

        self.assertEqual(
            text_to_textnodes(text),
            [
                TextNode("This text has ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("bold2", TextType.BOLD)
            ]
        ) 

    def test_text_to_node_bold_italic(self):
        text = "This text has **bold** and *italic*"

        self.assertEqual(
            text_to_textnodes(text),
            [
                TextNode("This text has ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC)
            ]
        ) 

    def test_text_to_node_italic_code(self):
        text = "This text has *italic* and `code`"

        self.assertEqual(
            text_to_textnodes(text),
            [
                TextNode("This text has ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" and ", TextType.TEXT),
                TextNode("code", TextType.CODE)
            ]
        ) 

    def test_text_to_node_bold_code(self):
        text = "This text has **bold** and `code`"

        self.assertEqual(
            text_to_textnodes(text),
            [
                TextNode("This text has ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("code", TextType.CODE)
            ]
        ) 

    def test_text_to_node_bold_italic_code(self):
        text = "This text has **bold** and *italic* and `code`"

        self.assertEqual(
            text_to_textnodes(text),
            [
                TextNode("This text has ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" and ", TextType.TEXT),
                TextNode("code", TextType.CODE)
            ]
        ) 
    
    def test_text_to_node_mult_bold_one_italic(self):
        text = "This text has **bold** and **bold2** and `code`"

        self.assertEqual(
            text_to_textnodes(text),
            [
                TextNode("This text has ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("bold2", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("code", TextType.CODE)
            ]
        ) 

    def test_text_to_node_bold_first_image(self):
        text = "This text has **bold** and ![google](https://google.com)"

        self.assertEqual(
            text_to_textnodes(text),
            [
                TextNode("This text has ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("google", TextType.IMAGE, "https://google.com")
            ]
        ) 

    def test_text_to_node_bold_end_image(self):
        text = "This text has ![google](https://google.com) and **bold**"

        self.assertEqual(
            text_to_textnodes(text),
            [
                TextNode("This text has ", TextType.TEXT),
                TextNode("google", TextType.IMAGE, "https://google.com"),
                TextNode(" and ", TextType.TEXT),
                TextNode("bold", TextType.BOLD)
            ]
        ) 

    def test_text_to_node_bold_first_link(self):
        text = "This text has **bold** and [google](https://google.com)"

        self.assertEqual(
            text_to_textnodes(text),
            [
                TextNode("This text has ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("google", TextType.LINK, "https://google.com")
            ]
        ) 

    def test_text_to_node_bold_link_before_image(self):
        text = "This text has **bold** and [google](https://google.com) with ![google](https://google.com)"

        self.assertEqual(
            text_to_textnodes(text),
            [
                TextNode("This text has ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("google", TextType.LINK, "https://google.com"),
                TextNode(" with ", TextType.TEXT),
                TextNode("google", TextType.IMAGE, "https://google.com")
            ]
        ) 

    def test_text_to_node_bold_image_before_link(self):
        text = "This text has **bold** and ![google](https://google.com) with [google](https://google.com)"

        self.assertEqual(
            text_to_textnodes(text),
            [
                TextNode("This text has ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("google", TextType.IMAGE, "https://google.com"),
                TextNode(" with ", TextType.TEXT),
                TextNode("google", TextType.LINK, "https://google.com")
            ]
        ) 

    def test_text_to_node_bold_end_link(self):
        text = "This text has [google](https://google.com) and **bold**"

        self.assertEqual(
            text_to_textnodes(text),
            [
                TextNode("This text has ", TextType.TEXT),
                TextNode("google", TextType.LINK, "https://google.com"),
                TextNode(" and ", TextType.TEXT),
                TextNode("bold", TextType.BOLD)
            ]
        ) 

    def test_text_to_node_all_together(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

        self.assertEqual(
            text_to_textnodes(text),
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
            ]
        )