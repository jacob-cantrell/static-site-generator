from split_node_functions import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT, None)]
    if "**" in text:
        nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    if "*" in text:
        nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    if "`" in text:
        nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes