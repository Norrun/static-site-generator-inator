from extract_data import get_node_recursive
from htmlnode import HTMLNode
from to_htmlnodes import markdown_to_html_node

def extract_title(markdown: str | HTMLNode):
    if markdown is str:
        markdown = markdown_to_html_node(markdown)
    node = get_node_recursive("h1", markdown,0)
    title = node.children[0].value
    return title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = ""
    with open(from_path) as mf:
        markdown = mf.read()
    template = ""
    with open(template_path) as tf:
        template = tf.read()

    # END DATAGRAB

    node = markdown_to_html_node(markdown)

    html = node.to_html()
    title = extract_title(node)

    titled = template.replace("{{ Title }}", title)
    page = titled.replace("{{ Content }}", html)

