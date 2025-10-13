import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        self.assertEqual( repr( HTMLNode(tag="h1", value="Hello", props={"class": "light"})) ,"\nh1( class=\"light\"){\nHello\n}\n")
    def test_props_to_html(self):
        node = HTMLNode(tag="a", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_props_to_html_single_prop(self):
        node = HTMLNode(tag="img", props={"src": "image.jpg"})
        self.assertEqual(node.props_to_html(), ' src="image.jpg"')

    def test_props_to_html_no_props(self):
        node = HTMLNode(tag="p", value="Hello")
        self.assertEqual(node.props_to_html(), '')

    def test_to_html_raises_error(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()