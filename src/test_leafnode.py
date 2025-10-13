import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_no_value_raises_error(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_leaf_no_tag_raw_text(self):
        node = LeafNode(None, "Just plain text")
        self.assertEqual(node.to_html(), "Just plain text")

    def test_leaf_longer_tag(self):
        node = LeafNode("span", "testing")
        self.assertEqual(node.to_html(),"<span>testing</span>")

    def test_leaf_multiple_props(self):
        node = LeafNode("a", "Link", {"href": "https://boot.dev", "target": "_blank"})
        self.assertEqual(node.to_html(),"<a href=\"https://boot.dev\" target=\"_blank\">Link</a>" )

if __name__ == "__main__":
    unittest.main()