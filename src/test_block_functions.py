import unittest
from block_functions import markdown_to_blocks

class TestBlockFunctions(unittest.TestCase):
    # TEST - MARKDOWN TO BLOCKS
    def test_md_to_block_one_block(self):
        markdown = "# This is just one block"

        self.assertEqual(
            markdown_to_blocks(markdown),
            [
                "# This is just one block"
            ]
        )

    def test_md_to_block_one_block_leading_and_trailing_whitespace(self):
        markdown = "     # This is just one block       "

        self.assertEqual(
            markdown_to_blocks(markdown),
            [
                "# This is just one block"
            ]
        )

    def test_md_to_block_one_block_leading_and_trailing_newline(self):
        markdown = "\n# This is just one block\n"

        self.assertEqual(
            markdown_to_blocks(markdown),
            [
                "# This is just one block"
            ]
        )

    def test_md_to_block_mult_blocks_one_blank_line_between(self):
        markdown = "# This is just one block\n\n## This is another block"

        self.assertEqual(
            markdown_to_blocks(markdown),
            [
                "# This is just one block",
                "## This is another block"
            ]
        )

    def test_md_to_block_mult_blocks_mult_blank_line_between(self):
        markdown = "# This is just one block\n\n\n## This is another block\n\n\n"

        self.assertEqual(
            markdown_to_blocks(markdown),
            [
                "# This is just one block",
                "## This is another block"
            ]
        )

    def test_md_to_block_one_block_with_internal_newlines(self):
        markdown = "# This is just one block\n\n* This is list item 1\n* List item 2\n* and list item 3"

        self.assertEqual(
            markdown_to_blocks(markdown),
            [
                "# This is just one block",
                "* This is list item 1\n* List item 2\n* and list item 3"
            ]
        )

        # TEST - BLOCK TO BLOCK TYPE