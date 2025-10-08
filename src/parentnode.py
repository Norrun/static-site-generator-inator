from htmlnode import HTMLNode
from functools import reduce 
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    def to_html(self):
        if self.tag is None:
            raise ValueError("tag is required")
        if self.children is None or len(self.children) == 0:
            raise ValueError("missing children")
        return f"<{self.tag}{self.props_to_html()}>{reduce(lambda x, y: x + y, map(lambda x: x.to_html(), self.children))}</{self.tag}>"
        