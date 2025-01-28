import unittest
from block_functions import markdown_to_blocks, block_to_block_type

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
    def test_block_to_type_heading1(self):
        self.assertEqual(
            block_to_block_type("# heading 1"),
            "heading"
        )

    def test_block_to_type_heading2(self):
        self.assertEqual(
            block_to_block_type("## heading 2"),
            "heading"
        )

    def test_block_to_type_heading3(self):
        self.assertEqual(
            block_to_block_type("### heading 3"),
            "heading"
        )

    def test_block_to_type_heading4(self):
        self.assertEqual(
            block_to_block_type("#### heading 4"),
            "heading"
        )

    def test_block_to_type_heading5(self):
        self.assertEqual(
            block_to_block_type("##### heading 5"),
            "heading"
        )

    def test_block_to_type_heading6(self):
        self.assertEqual(
            block_to_block_type("###### heading 6"),
            "heading"
        )

    def test_block_to_type_quote_one_line(self):
        self.assertEqual(
            block_to_block_type("> quote 1"),
            "quote"
        )

    def test_block_to_type_quote_mult_line(self):
        self.assertEqual(
            block_to_block_type("> quote 1\n> quote 2"),
            "quote"
        )

    def test_block_to_type_code(self):
        self.assertEqual(
            block_to_block_type("``` code ```"),
            "code"
        )

    def test_block_to_type_uo_list_asterik(self):
        self.assertEqual(
            block_to_block_type("* test 1\n* test 2\n* test 3"),
            "unordered_list"
        )

    def test_block_to_type_uo_list_dash(self):
        self.assertEqual(
            block_to_block_type("- test 1\n- test 2\n- test 3"),
            "unordered_list"
        )

    def test_block_to_type_uo_list_asterik_and_dash(self):
        self.assertEqual(
            block_to_block_type("* test 1\n- test 2\n* test 3"),
            "unordered_list"
        )

    def test_block_to_type_ordered_list(self):
        self.assertEqual(
            block_to_block_type("1. test 1\n2. test 2\n3. test 3"),
            "ordered_list"
        )

    def test_block_to_type_ordered_list_unsequenced(self):
        self.assertEqual(
            block_to_block_type("1. test 1\n3. test 2\n2. test 3"),
            "paragraph"
        )

    def test_block_to_type_paragraph(self):
        self.assertEqual(
            block_to_block_type("this is just text so it's a paragraph"),
            "paragraph"
        )