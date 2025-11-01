from enum import Enum 
import re
from htmlnode import HTMLNode
class BlockType(Enum):
    PARAGRAPH = 1
    HEADING = 2
    CODE = 3
    QUOTE = 4
    UNORDERED_LIST = 5
    ORDERED_LIST = 6

def markdown_to_blocks(markdown: str):
    blocks = re.split(r"\n\s*\n",markdown)
    blocks = filter(lambda b: b != "",map(lambda b : b.strip(),blocks))
    return list(blocks)

def block_to_blocktype(block: str):
    if re.fullmatch(r"#{1,6} .+\n?",block) is not None:
        return BlockType.HEADING
    if re.fullmatch(r"```[\w\d]*\n[\S\s]*\n```",block) is not None:
        return BlockType.CODE
    if re.fullmatch(r"((\n|^)>.*)*\n?",block) is not None:
        return BlockType.QUOTE
    if re.fullmatch(r"((\n|^)- .*)*\n?",block) is not None:
        return BlockType.UNORDERED_LIST
    if ordered_list_helper(block):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
    
def ordered_list_helper(block: str):
    lines = block.splitlines()
    for i in range(0,len(lines)):
        if not lines[i].startswith(f"{i + 1}. "):
            return False
    return True

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_blocktype(block)

def select_heading(heading_block):
    m = re.match(r"#{1,6}",heading_block)
    if m is None:
        raise ValueError("invalid heading block")
    level = len(m[0])
    


def list_assembler(ordered_list):
    pass

def unordered_lits_assembler(unordered_lits):
    pass