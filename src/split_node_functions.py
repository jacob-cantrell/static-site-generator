from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    text_node_list = []

    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            text_node_list.append(node)
            continue
        elif not node.text.count(delimiter) == 2:
            raise Exception("Invalid Markup syntax! No matching enclosing delimiter detected!")
        
        split_by_delim = node.text.split(delimiter)
        node_list = []
        if not split_by_delim[0] == "":
            node_list.append(TextNode(split_by_delim[0], node.text_type, node.url))
        node_list.append(TextNode(split_by_delim[1], text_type, node.url))
        if not split_by_delim[2] == "":
            node_list.append(TextNode(split_by_delim[2], node.text_type, node.url))

        text_node_list.extend(node_list)

    return text_node_list

def split_nodes_images(old_nodes):
    pass

def split_nodes_links(old_nodes):
    pass