import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
    )
    
    def test_tag_none_value_error(self):
        child_node = LeafNode("p", "test")
        parent_node = ParentNode(None,[child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()
    
    def test_children_none_value_error(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()
    
    def test_props(self):
        child_node = LeafNode("p", "test")
        parent_node = ParentNode("div",[child_node],{"id": "main", "class": "container content", "style": "color:red; margin:0"})
        self.assertEqual(parent_node.to_html(), "<div id=\"main\" class=\"container content\" style=\"color:red; margin:0\"><p>test</p></div>")
    
    def test_child_mix(self):
        grand_child = LeafNode("p", "test")
        child_node = ParentNode("div",[grand_child])
        brother_node = LeafNode("h1", "testing")
        parent_node = ParentNode("div", [brother_node,child_node])
        self.assertEqual(parent_node.to_html(), "<div><h1>testing</h1><div><p>test</p></div></div>")

    def test_child_mix_inner_props(self):
        grand_child = LeafNode("p", "test")
        child_node = ParentNode("div",[grand_child],{"id": "main", "class": "container content", "style": "color:red; margin:0"})
        brother_node = LeafNode("h1", "testing")
        parent_node = ParentNode("div", [brother_node,child_node])
        self.assertEqual(parent_node.to_html(), "<div><h1>testing</h1><div id=\"main\" class=\"container content\" style=\"color:red; margin:0\"><p>test</p></div></div>")

    if __name__ == "__main__":
        unittest.main()