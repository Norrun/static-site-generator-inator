from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode

def extract_stuff(tag, node: HTMLNode, jump = 0 ):
    if node.tag != tag:
        if node is ParentNode:
            for node in node.children:
                res, jum = extract_stuff(tag,node,jump)
                if res is None:
                    continue
                if ...

        else:
            return None, jump
    else:
        if jump > 0:
           
    