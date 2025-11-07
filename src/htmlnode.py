
class HTMLNode:
    def __init__(self, tag=None, value=None, 
                 children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    def props_to_html(self):
        if self.props is None:
            return ""
        result = ""
        for prop in self.props:
            result += f" {prop}=\"{self.props[prop]}\""
        return result
    def __repr__(self):
        children = ""
        if self.children is not None:
            for child in self.children:
                children += repr(child) + "\n"
        return f"""
{self.tag}({self.props_to_html()}){ "{\n"+ self.value + "\n" + children + "}"}
"""
        