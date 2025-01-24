import unittest
from extract_markdown_functions import extract_markdown_image, extract_markdown_link

class TestExtractMarkdownFunctions(unittest.TestCase):
    def test_no_markdown_found_image(self):
        text = "This is just text"
        self.assertEqual(
            extract_markdown_image(text),
            []
        )

    def test_one_markdown_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        self.assertEqual(
            extract_markdown_image(text),
            [("rick roll", "https://i.imgur.com/aKaOqIh.gif")]
        )

    def test_two_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(
            extract_markdown_image(text),
            [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        )

    def test_markdown_image_with_link_markdown(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev)"
        self.assertEqual(
            extract_markdown_image(text),
            []
        )

    def test_no_markdown_found_link(self):
        text = "This is just text"
        self.assertEqual(
            extract_markdown_link(text),
            []
        )

    def test_one_markdown_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev)"
        self.assertEqual(
            extract_markdown_link(text),
            [("to boot dev", "https://www.boot.dev")]
        )

    def test_two_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(
            extract_markdown_link(text),
            [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        )

    def test_markdown_link_with_image_markdown(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        self.assertEqual(
            extract_markdown_link(text),
            []
        )