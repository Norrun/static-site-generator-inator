import re
from textnode import TextNode, TextType

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches 

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        matches = extract_markdown_images(node.text)
        if len(matches) == 0:
            new_nodes.append(node)
            continue
        next_section = node.text
        for m in matches:
            sections = next_section.split(f"![{m[0]}]({m[1]})", 1)
            if sections[0] != "" :
                new_nodes.append(TextNode(sections[0], TextType.PLAIN))
            new_nodes.append(TextNode(m[0],TextType.IMAGE,m[1]))
            if sections[1] != "" :
                next_section = sections[1]
        #new_nodes.append(next_section)
    return new_nodes


def split_nodes_links(old_nodes):
    new_nodes = []
    for node in old_nodes:
        matches = extract_markdown_links(node.text)
        if len(matches) == 0:
            new_nodes.append(node)
            continue
        for m in matches:
            sections = node.text.split(f"[{m[0]}]({m[1]})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.PLAIN))
            new_nodes.append(TextNode(m[0],TextType.LINK,m[1]))
            if sections[1] != "":
                new_nodes.append(TextNode(sections[1], TextType.PLAIN))
    return new_nodes

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter, text_type: TextType):
    new_nodes = []
    for node in old_nodes:
        print(node)
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue
        texts = node.text.split(delimiter)
        if len(texts) == 1:
            new_nodes.append(node)
            continue
        if len(texts) % 2 != 1:
            raise Exception("invalid markdown syntax")
        for i in range(0, len(texts)):
            if i % 2 == 0:
                if texts[i] != "":
                    new_nodes.append(TextNode(texts[i], TextType.PLAIN))
            else:
                new_nodes.append(TextNode(texts[i],text_type))
    return new_nodes

def text_to_textnodes(text):
    nodes = split_nodes_delimiter([TextNode(text, text_type=TextType.PLAIN)],"**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes,"_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes,"`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_links(nodes)
    return nodes