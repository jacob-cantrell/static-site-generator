import unittest
from block_functions import markdown_to_blocks, block_to_block_type, get_heading_number, markdown_to_html_node

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

    # TEST - MARKDOWN TO HTML NODE
    def test_get_heading_number_1(self):
        self.assertEqual(
            get_heading_number("# test"),
            1
        )

    def test_get_heading_number_2(self):
        self.assertEqual(
            get_heading_number("## test"),
            2
        )

    def test_get_heading_number_3(self):
        self.assertEqual(
            get_heading_number("### test"),
            3
        )

    def test_get_heading_number_4(self):
        self.assertEqual(
            get_heading_number("#### test"),
            4
        )

    def test_get_heading_number_5(self):
        self.assertEqual(
            get_heading_number("##### test"),
            5
        )

    def test_get_heading_number_6(self):
        self.assertEqual(
            get_heading_number("###### test"),
            6
        )

    def test_simple_heading1(self):
        self.assertEqual(
            markdown_to_html_node("# Heading 1 Test").to_html(),
            "<div><h1>Heading 1 Test</h1></div>"
        )

    def test_simple_heading2(self):
        self.assertEqual(
            markdown_to_html_node("## Heading 2 Test").to_html(),
            "<div><h2>Heading 2 Test</h2></div>"
        )

    def test_simple_heading3(self):
        self.assertEqual(
            markdown_to_html_node("### Heading 3 Test").to_html(),
            "<div><h3>Heading 3 Test</h3></div>"
        )

    def test_simple_heading4(self):
        self.assertEqual(
            markdown_to_html_node("#### Heading 4 Test").to_html(),
            "<div><h4>Heading 4 Test</h4></div>"
        )

    def test_simple_heading5(self):
        self.assertEqual(
            markdown_to_html_node("##### Heading 5 Test").to_html(),
            "<div><h5>Heading 5 Test</h5></div>"
        )

    def test_simple_heading6(self):
        self.assertEqual(
            markdown_to_html_node("###### Heading 6 Test").to_html(),
            "<div><h6>Heading 6 Test</h6></div>"
        )

    def test_paragraph_no_special_text(self):
        self.assertEqual(
            markdown_to_html_node("This is a test paragraph").to_html(),
            "<div><p>This is a test paragraph</p></div>"
        )

    def test_paragraph_with_bold_text(self):
        self.assertEqual(
            markdown_to_html_node("This is a test **bold** paragraph").to_html(),
            "<div><p>This is a test <strong>bold</strong> paragraph</p></div>"
        )

    def test_valid_ul_list_item_no_special_text(self):
        self.assertEqual(
            markdown_to_html_node("- test 1\n- test 2\n- test 3\n").to_html(),
            "<div><ul><li>test 1</li><li>test 2</li><li>test 3</li></ul></div>"
        )

    def test_valid_ol_list_item_no_special_text(self):
        self.assertEqual(
            markdown_to_html_node("1. test 1\n2. test 2\n3. test 3\n").to_html(),
            "<div><ol><li>test 1</li><li>test 2</li><li>test 3</li></ol></div>"
        )

    def test_valid_link_no_text(self):
        self.assertEqual(
            markdown_to_html_node("[test](https://google.com)").to_html(),
            "<div><a href=\"https://google.com\">test</a></div>"
        )

    def test_valid_image(self):
        self.assertEqual(
            markdown_to_html_node("![test](https://google.com)").to_html(),
            "<div><img src=\"https://google.com\" alt=\"test\"></img></div>"
        )

    def test_valid_link_and_image(self):
        self.assertEqual(
            markdown_to_html_node("[test](https://google.com)\n\n![test](https://google.com)").to_html(),
            "<div><a href=\"https://google.com\">test</a><img src=\"https://google.com\" alt=\"test\"></img></div>"
        )

    def test_valid_code_block(self):
        self.assertEqual(
            markdown_to_html_node("```This is a test```").to_html(),
            "<div><pre><code>This is a test</code></pre></div>"
        )

    def test_valid_quote_block(self):
        self.assertEqual(
            markdown_to_html_node("> text\n> text 2\n> text 3\n").to_html(),
            "<div><blockquote>text\ntext 2\ntext 3</blockquote></div>"
        )

    def test_large_combination(self):
        markdown = "# Header\n\nThis is just a paragraph with **bold** and *italic* text\n\n```with code```\n\n> and\n> quotes"
        self.assertEqual(
            markdown_to_html_node(markdown).to_html(),
            "<div><h1>Header</h1><p>This is just a paragraph with <strong>bold</strong> and <em>italic</em> text</p><pre><code>with code</code></pre><blockquote>and\nquotes</blockquote></div>"
        )

    def test_Large_combination(self):
        markdown = "[link](https://google.com)\n\n![image](https://google.com)\n\n* ul1\n- ul2\n* ul3\n\n1. ol1\n2. ol2\n3. ol3"
        self.assertEqual(
            markdown_to_html_node(markdown).to_html(),
            "<div><a href=\"https://google.com\">link</a><img src=\"https://google.com\" alt=\"image\"></img><ul><li>ul1</li><li>ul2</li><li>ul3</li></ul><ol><li>ol1</li><li>ol2</li><li>ol3</li></ol></div>"
        )