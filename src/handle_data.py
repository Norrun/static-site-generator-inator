from extract_data import get_node_recursive
from htmlnode import HTMLNode
from to_htmlnodes import markdown_to_html_node

def extract_title(markdown: str | HTMLNode):
    if markdown is str:
        markdown = markdown_to_html_node(markdown)
    node = get_node_recursive("h1", markdown,0)
    title = node.children[0].value
    return title
