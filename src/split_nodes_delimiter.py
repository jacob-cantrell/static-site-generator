from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    text_node_list = []

    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            text_node_list.append(node)
            continue
        elif not node.text.count(delimiter) == 2:
            raise Exception("Invalid Markup syntax! No matching enclosing delimiter detected!")
        
        
            
    return text_node_list