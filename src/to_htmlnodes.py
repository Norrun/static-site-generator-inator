from parentnode import ParentNode
from leafnode import LeafNode
from blocks import BlockType, markdown_to_blocks, block_to_blocktype
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
                pass

                




def create_heading(heading_block):
    m = re.match(r"#{1,6}",heading_block)
    if m is None:
        raise ValueError("invalid heading block")
    level = len(m[0])

def create_code(code_block):
    pass

def process_leafs(content):
    pass