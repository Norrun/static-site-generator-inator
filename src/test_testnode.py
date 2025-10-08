import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_diff_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is different text", TextType.BOLD)
        self.assertNotEqual(node, node2)
    def test_diff_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    def test_diff_url(self):
        node = TextNode("Link", TextType.LINK, url="https://boot.dev")
        node2 = TextNode("Link", TextType.LINK, url="https://google.com")
        self.assertNotEqual(node, node2)
    def test_eq_none_url(self):
        node = TextNode("Text with no URL", TextType.PLAIN, url=None)
        node2 = TextNode("Text with no URL", TextType.PLAIN, url=None)
        self.assertEqual(node, node2)
    def test_diff_none_url(self):
        node = TextNode("Link", TextType.LINK, url="https://boot.dev")
        node2 = TextNode("Link", TextType.LINK, url=None)
        self.assertNotEqual(node, node2)
    def test_text(self):
        node = TextNode("This is a text node", TextType.PLAIN)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

if __name__ == "__main__":
    unittest.main()