from main import split_nodes_delimiter
from textnode import TextNode, TextType
import unittest

class TestNodeSplit(unittest.TestCase):
    def test_first(self):
        node = TextNode("This is text with a **bolded phrase** in the middle",TextType.PLAIN)
        split = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(split,[
    TextNode("This is text with a ", TextType.PLAIN),
    TextNode("bolded phrase", TextType.BOLD),
    TextNode(" in the middle", TextType.PLAIN),
])
        

if __name__ == "__main__":
    unittest.main()