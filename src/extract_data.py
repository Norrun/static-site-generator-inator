from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode



def get_node_recursive(tag, node: HTMLNode, skip = 0 ):
    if node.tag == tag:
        if skip <= 0:
            return node
        skip -= 1
    
    if node is ParentNode:
        for node in node.children:
            res = get_node_recursive(tag,node,skip)
            if res is None:
                continue
            if skip > 0:
                skip -= 1
                continue
            return res
    return None
    
    



    
           
    