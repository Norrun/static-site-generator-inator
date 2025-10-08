from textnode import *

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
        if len(texts) % 3 != 0:
            raise Exception("invalid markdown syntax")
        for i in range(0, len(texts)):
            if i % 2 == 0:
                if texts[i] != "":
                    new_nodes.append(TextNode(texts[i], TextType.PLAIN))
            else:
                new_nodes.append(TextNode(texts[i],text_type))
    return new_nodes
        

def main():
    node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(node)
main()