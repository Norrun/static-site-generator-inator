import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        self.assertEqual( repr( HTMLNode(tag="h1", value="Hello", props={"class": "light"})) ,"\nh1( class=\"light\"){\nHello\n}\n")