from parentnode import ParentNode
from leafnode import LeafNode
from textnode import TextNode, TextType
from blocks import BlockType, markdown_to_blocks, block_to_blocktype
from text_logic import text_to_textnodes
from textnode import text_node_to_html_node
import re

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        block_type = block_to_blocktype(block)
        match block_type:
            case BlockType.HEADING:
                node = create_heading(block)
                nodes.append(node)
            case BlockType.CODE:
                node = create_code(block)
                nodes.append(node)

            case BlockType.QUOTE:
                node = create_quote(block)
                nodes.append(node)
            case BlockType.UNORDERED_LIST:
                node = create_ordered_list(block)
                nodes.append(node)
            case BlockType.ORDERED_LIST:
                node = create_ordered_list(block)
                nodes.append(node)
            case BlockType.PARAGRAPH:
                node = create_paragraph(block)
                nodes.append(node)
                
    return ParentNode("div", nodes)


                

def create_paragraph(paragraph:str):
    children = process_leafs(paragraph)
    node = ParentNode("p", children)
    return node



def create_heading(heading_block):
    m = re.match(r"#{1,6}",heading_block)
    if m is None:
        raise ValueError("invalid heading block")
    level = len(m[0])
    children = process_leafs(m[0][level + 1 :])
    tag = f"h{level}"
    return ParentNode(tag,children)


def create_code(code_block: str):
    lines =  code_block.split("\n")
    syntax_removed = lines[1:-1]
    value = "\n".join(syntax_removed) + "\n"
    text_node = TextNode(value,TextType.PLAIN)
    inner_node = text_node_to_html_node(text_node)
    code = ParentNode("code",[inner_node])
    pre = ParentNode("pre",[code])
    return pre


def create_quote(quote: str):
    lines = quote.splitlines()
    strippeds = []
    for line in lines:
        stripped = line.lstrip("> ")
        strippeds.append(stripped)
    
    value = "\n".join(strippeds)
    children = process_leafs(value)
    return ParentNode("blockquote",children)


def create_ordered_list(list: str):
    lines = list.split("\n")
    nodes = []
    for line in lines:
        # TODO test split with space to simplify function
        post_dot = line.split(".", maxsplit = 1)[1]
        value = post_dot.lstrip()
        children = process_leafs(value)
        done = ParentNode("li",children)
        nodes.append(done)
    return ParentNode("ol",nodes)

def create_unordered_list(list: str):
    lines = list.split("\n")
    nodes = []
    for line in lines:
        stripped = line.lstrip("- ")
        children = process_leafs(stripped)
        done = ParentNode("li", children)
        nodes.append(done)
    return ParentNode("ul", nodes)

def create_paragraph(paragraph: str):
    paragraph = paragraph.replace("\n"," ")
    children = process_leafs(paragraph)
    return ParentNode("p",children)


def process_leafs(content):
    tnodes = text_to_textnodes(content)
    return list(map(text_node_to_html_node,tnodes))

