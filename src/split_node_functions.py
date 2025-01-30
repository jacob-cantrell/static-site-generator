from extract_markdown_functions import extract_markdown_image, extract_markdown_link
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    text_node_list = [] # Empty list
    for node in old_nodes: # Check every node passed in as parameter
        # If TextType of node is not TEXT/NORMAL, append to list and move on per prompt
        if node.text_type is not TextType.TEXT:
            text_node_list.append(node)
            continue
        # Otherwise all checks are valid and traverse the text for markdown
        else:
            split_text = node.text.split(delimiter) # Split the text for creating new Nodes
            node_list = [] # List for new nodes being created to be extended onto final list
            for i in range(0, len(split_text)):
                # If even index, will be normal text string
                if i % 2 == 0:
                    # If valid text string (not None and not empty), then create node and add to list
                    if not split_text[i] == "":
                        node_list.append(TextNode(split_text[i], TextType.TEXT, node.url))
                else: # Odd index
                    # Append new node to list with special text
                    node_list.append(TextNode(split_text[i], text_type, node.url))
            text_node_list.extend(node_list)

    return text_node_list

def split_nodes_image(old_nodes):
    text_node_list = []

    # Traverse nodes in old_nodes list passed in as parameter
    for node in old_nodes:
        # If not image markdown found, append original to list
        if node.text is None or node.text == "":
            continue
        elif extract_markdown_image(node.text) == []:
            text_node_list.append(node)
        else:
            node_list = [] # List of new TextNodes
            # Otherwise, split node text and create new TextNodes
            # Find number of image markdowns in text for splitting purposes
            images = extract_markdown_image(node.text)
            if len(images) == 1: # Only need to split once and append TextNodes
                text = node.text.split(f"![{images[0][0]}]({images[0][1]})")
                if not text[0] == "":
                    node_list.append(
                        TextNode(text[0], node.text_type, node.url)
                    )
                node_list.append(
                    TextNode(images[0][0], TextType.IMAGE, images[0][1])
                )
                if not text[1] == "":
                    node_list.append(
                        TextNode(text[1], node.text_type, node.url)
                    )
            else: # More than 1 image markdown found
                new_text = node.text
                for i in range(0, len(images)): # For each tuple in list, split
                    split_txt = new_text.split(f"![{images[i][0]}]({images[i][1]})", 1) # Split text
                    # Check first text - if empty, move on; if not, add new TextNode to node_list
                    if not split_txt[0] == "":
                        node_list.append(
                            TextNode(split_txt[0], node.text_type, node.url)
                        )
                    # Add image node to node_list
                    node_list.append(
                        TextNode(images[i][0], TextType.IMAGE, images[i][1])
                    )
                    # If last split (i+1 == len(images)), then check second text
                    if i + 1 == len(images):
                        if not split_txt[1] == "":
                            node_list.append(
                                TextNode(split_txt[1], node.text_type, node.url)
                            )
                    # Otherwise, another split is required; adjust new_text and continue
                    else:
                        new_text = split_txt[1]
            text_node_list.extend(node_list)

    return text_node_list


def split_nodes_link(old_nodes):
    text_node_list = []

    # Traverse nodes in old_nodes list passed in as parameter
    for node in old_nodes:
        # If not link markdown found, append original to list
        if node.text is None or node.text == "":
            continue
        elif extract_markdown_link(node.text) == []:
            text_node_list.append(node)
        else:
            node_list = [] # List of new TextNodes
            # Otherwise, split node text and create new TextNodes
            # Find number of link markdowns in text for splitting purposes
            links = extract_markdown_link(node.text)
            if len(links) == 1: # Only need to split once and append TextNodes
                text = node.text.split(f"[{links[0][0]}]({links[0][1]})")
                if not text[0] == "":
                    node_list.append(
                        TextNode(text[0], node.text_type, node.url)
                    )
                node_list.append(
                    TextNode(links[0][0], TextType.LINK, links[0][1])
                )
                if not text[1] == "":
                    node_list.append(
                        TextNode(text[1], node.text_type, node.url)
                    )
            else: # More than 1 image markdown found
                new_text = node.text
                for i in range(0, len(links)): # For each tuple in list, split
                    split_txt = new_text.split(f"[{links[i][0]}]({links[i][1]})", 1) # Split text
                    # Check first text - if empty, move on; if not, add new TextNode to node_list
                    if not split_txt[0] == "":
                        node_list.append(
                            TextNode(split_txt[0], node.text_type, node.url)
                        )
                    # Add image node to node_list
                    node_list.append(
                        TextNode(links[i][0], TextType.LINK, links[i][1])
                    )
                    # If last split (i+1 == len(links)), then check second text
                    if i + 1 == len(links):
                        if not split_txt[1] == "":
                            node_list.append(
                                TextNode(split_txt[1], node.text_type, node.url)
                            )
                    # Otherwise, another split is required; adjust new_text and continue
                    else:
                        new_text = split_txt[1]
            text_node_list.extend(node_list)

    return text_node_list