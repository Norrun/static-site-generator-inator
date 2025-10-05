import unittest

from textnode import TextNode, TextType


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

if __name__ == "__main__":
    unittest.main()