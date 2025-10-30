from enum import Enum 
import re
class BlockType(Enum):
    PARAGRAPH = 1
    HEADING = 2
    CODE = 3
    QUOTE = 4
    UNORDERED_LIST = 5
    ORDERED_LIST = 6

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