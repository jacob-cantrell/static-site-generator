import unittest
from generate_page import extract_title

class TestGeneratePage(unittest.TestCase):
    # EXTRACT TITLE TESTS
    def test_extract_title_1(self):
        markdown = "# Hello"
        self.assertEqual(
            extract_title(markdown),
            "Hello"
        )

    def test_extract_title_2(self):
        markdown = "# Hello World"
        self.assertEqual(
            extract_title(markdown),
            "Hello World"
        )

    def test_extract_title_2(self):
        markdown = "# Hello World"
        self.assertRaises(
            Exception,
            extract_title(markdown)
        )