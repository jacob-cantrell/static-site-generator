from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("No value detected!")
        elif self.tag is None:
            return f"{self.value}"
        elif self.props is None or len(self.props) == 0:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}" + self.props_to_html() + f">{self.value}</{self.tag}>"