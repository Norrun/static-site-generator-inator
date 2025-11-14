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
                create_code(block)

            case BlockType.QUOTE:
                create_quote(block)

                

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
    value = "\n".join(syntax_removed)
    text_node = TextNode(value,TextType.PLAIN)
    inner_node = text_node_to_html_node(text_node)
    code = ParentNode("code",[inner_node])
    pre = ParentNode("pre",[code])
    return pre


def create_quote(quote: str):
    value = quote.replace("> ","")


def process_leafs(content):
    tnodes = text_to_textnodes(content)
    return list(map(text_node_to_html_node,tnodes))

