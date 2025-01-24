from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Missing tag - none detected!")
        elif self.children is None:
            raise ValueError("Missing children - none detected!")
        
        if self.props is None or len(self.props) == 0:
            str = f"<{self.tag}>"
        else:
            str = f"<{self.tag}" + self.props_to_html() + ">"

        for node in self.children:
            str += node.to_html()
        
        return str + f"</{self.tag}>"