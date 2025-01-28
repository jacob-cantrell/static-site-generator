import re

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