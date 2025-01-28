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
    pass