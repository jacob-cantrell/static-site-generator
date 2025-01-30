import re
from parentnode import ParentNode
from leafnode import LeafNode
from text_to_textnodes import text_to_textnodes
from textnode import TextType

def markdown_to_blocks(markdown):
    # Empty string list we are adding blocks to
    str_list = []

    # Split markdown into lines (empty lines represent break between blocks)
    lines = markdown.strip().split("\n\n")

    # Traverse lines and add blocks to str_list; check if block is just an empty string or newline
    for block in lines:
        if block.strip() != "":
            str_list.append(block.strip())

    return str_list

def block_to_block_type(block):
    if re.search(r"^#{1,6} ", block):
        return "heading"
    elif re.search(r"^```.*```$", block):
        return "code"
    elif re.search(r"^>.*(?:\n^>.*)*$", block, re.M):
        return "quote"
    elif re.search(r"^(\*|-) .*(?:\n^(\*|-) .*)*$", block, re.M):
        return "unordered_list"
    elif re.search(r"^1\. .*(?:\n^[2-9]\. .*)*$", block, re.M):
        lines = block.strip().split("\n")
        ol = True
        for i in range(0, len(lines)):
            number_str = lines[i].split('.')[0]  # Get text before the period
            try:
                number = int(number_str)  # Convert to integer
                if number != i + 1:
                    ol = False
                    break
            except ValueError:
                ol = False
                break
        if ol:
            return "ordered_list"
        else:
            return "paragraph"
    else:
        return "paragraph"

def get_heading_number(block):
    return len(block) - len(block.lstrip("#"))

def block_to_text(block, block_type):
    text = ""
    match (block_type):
            case "heading":
                text = block.lstrip("#")
                text = text.lstrip()
                return text
            case "code":
                text = block.strip("```")
                return text
            case "quote":
                text = block.replace("> ", "")
                return text
            case "unordered_list":
                lines = block.split("\n")
                new_lines = []
                for line in lines:
                    new_lines.append(line.lstrip("* -"))
                text = "\n".join(new_lines)
                return text
            case "ordered_list":
                lines = block.split("\n")
                new_lines = []
                for line in lines:
                    new_lines.append(line[(line.index(".") + 2):])
                text = "\n".join(new_lines)
                return text
            case "paragraph":
                return block
            case _:
                raise Exception("Invalid Markdown Syntax!")

def text_to_children(text):
    children = []
    text_nodes = text_to_textnodes(text)
    for node in text_nodes:
        match (node.text_type):
            case (TextType.TEXT):
                children.append(
                    LeafNode(None, node.text, None)
                )
            case (TextType.BOLD):
                children.append(
                    LeafNode("b", node.text, None)
                )
            case (TextType.ITALIC):
                children.append(
                    LeafNode("i", node.text, None)
                )
            case (TextType.CODE):
                children.append(
                    LeafNode("code", node.text, None)
                )
            case (TextType.LINK):
                children.append(
                    LeafNode("a", node.text, {"href": node.url})
                )
            case (TextType.IMAGE):
                children.append(
                    LeafNode("img", "", {"src": node.url, "alt": node.text})
                )
    return children

def markdown_to_html_node(markdown):
    # split markdown into blocks
    blocks = markdown_to_blocks(markdown)
    parent_div = ParentNode("div", [], {})

    # Iterate over the blocks
    for block in blocks:
        block_type = block_to_block_type(block)
        match (block_type):
            case "heading":
                parent_div.children.append(
                    ParentNode(f"h{get_heading_number(block)}", text_to_children(block_to_text(block, block_type)), {})
                )
            case "code":
                parent_div.children.append(
                    ParentNode("pre", 
                             [
                                 LeafNode("code", block_to_text(block, block_type), {})
                             ], 
                             {})
                )
            case "quote":
                parent_div.children.append(
                    ParentNode("blockquote", text_to_children(block_to_text(block, block_type)), {})
                )
            case "unordered_list":
                lines = block_to_text(block, block_type).split("\n")
                item_list = []
                for line in lines:
                    item_list.append(
                        ParentNode("li", text_to_children(line), {})
                    )

                parent_div.children.append(
                    ParentNode("ul", item_list, {})
                )
            case "ordered_list":
                lines = block_to_text(block, block_type).split("\n")
                item_list = []
                for line in lines:
                    item_list.append(
                        ParentNode("li", text_to_children(line), {})
                    )

                parent_div.children.append(
                    ParentNode("ol", item_list, {})
                )
            case "paragraph":
                if block.startswith("!["):
                    parent_div.children.extend(
                        text_to_children(block_to_text(block, block_type))
                    )
                elif "[" in block and "](" in block:
                    parent_div.children.extend(
                        text_to_children(block_to_text(block, block_type))
                    )
                else:
                    parent_div.children.append(
                        ParentNode("p", text_to_children(block_to_text(block, block_type)), {})
                    )
            case _:
                raise Exception("Invalid Markdown Syntax!")
            
    return parent_div