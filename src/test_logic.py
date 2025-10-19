import unittest
import logic
from textnode import TextNode, TextType


class TestLogic(unittest.TestCase):
    

    def test_code_block_middle(self):
        node = TextNode("This is text with a `code block` word", TextType.PLAIN)
        new_nodes = logic.split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is text with a ", TextType.PLAIN),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.PLAIN),
        ]
        self.assertListEqual(new_nodes, expected)
    
    def test_bold_multiple(self):
        node = TextNode("This is **bold** and this is also **bold**", TextType.PLAIN)
        new_nodes = logic.split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This is ", TextType.PLAIN),
            TextNode("bold", TextType.BOLD),
            TextNode(" and this is also ", TextType.PLAIN),
            TextNode("bold", TextType.BOLD),
        ]
        self.assertListEqual(new_nodes, expected)
    
    def test_delimiter_at_start(self):
        node = TextNode("_italic_ at start", TextType.PLAIN)
        new_nodes = logic.split_nodes_delimiter([node], "_", TextType.ITALIC)
        expected = [
            TextNode("italic", TextType.ITALIC),
            TextNode(" at start", TextType.PLAIN),
        ]
        self.assertListEqual(new_nodes, expected)

    def test_delimiter_at_end(self):
        node = TextNode("at end **bold**", TextType.PLAIN)
        new_nodes = logic.split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("at end ", TextType.PLAIN),
            TextNode("bold", TextType.BOLD),
        ]
        self.assertListEqual(new_nodes, expected)
    
    def test_only_delimited_text(self):
        node = TextNode("**all bold**", TextType.PLAIN)
        new_nodes = logic.split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("all bold", TextType.BOLD),
        ]
        self.assertListEqual(new_nodes, expected)

    def test_no_delimiter(self):
        node = TextNode("plain text with no formatting", TextType.PLAIN)
        new_nodes = logic.split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("plain text with no formatting", TextType.PLAIN),
        ]
        self.assertListEqual(new_nodes, expected)
    
    def test_non_text_node_unchanged(self):
        node = TextNode("already bold", TextType.BOLD)
        new_nodes = logic.split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("already bold", TextType.BOLD),
        ]
        self.assertListEqual(new_nodes, expected)
    
    def test_multiple_nodes_mixed(self):
        nodes = [
            TextNode("First `code` text", TextType.PLAIN),
            TextNode("already italic", TextType.ITALIC),
            TextNode("Second `code` text", TextType.PLAIN),
        ]
        new_nodes = logic.split_nodes_delimiter(nodes, "`", TextType.CODE)
        expected = [
            TextNode("First ", TextType.PLAIN),
            TextNode("code", TextType.CODE),
            TextNode(" text", TextType.PLAIN),
            TextNode("already italic", TextType.ITALIC),
            TextNode("Second ", TextType.PLAIN),
            TextNode("code", TextType.CODE),
            TextNode(" text", TextType.PLAIN),
        ]
        self.assertListEqual(new_nodes, expected)
    
    def test_unmatched_delimiter_raises_exception(self):
        node = TextNode("This has **no closing delimiter", TextType.PLAIN)
        with self.assertRaises(Exception):
            logic.split_nodes_delimiter([node], "**", TextType.BOLD)
    
    def test_second_unmatched_delimiter_raises_exception(self):
        node = TextNode("This has **no closing delimiter** on the **second one", TextType.PLAIN)
        with self.assertRaises(Exception):
            logic.split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_regex_image(self):
        maches = logic.extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")
        self.assertEqual(maches, [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])
    def test_regex_link(self):
        matches = logic.extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        self.assertListEqual(matches,[("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])

    def test_extract_multiple_images(self):
        text = "![first](url1) some text ![second](url2)"
        matches = logic.extract_markdown_images(text)
        self.assertListEqual([("first", "url1"), ("second", "url2")], matches)
    
    def test_extract_no_images(self):
        text = "This is just plain text with no images"
        matches = logic.extract_markdown_images(text)
        self.assertListEqual([], matches)

    def test_extract_link_with_image(self):
        text = "[first](url1) some text ![second](url2)"
        matches = logic.extract_markdown_links(text)
        self.assertListEqual([("first", "url1")], matches)
    
    def test_extract_image_with_link(self):
        text = "[first](url1) some text ![second](url2)"
        matches = logic.extract_markdown_images(text)
        self.assertListEqual([("second", "url2")], matches)
        
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN,
        )
        new_nodes = logic.split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN,
        )
        new_nodes = logic.split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    
    def test_split_link_none(self):
        node = TextNode("Just plain text.", TextType.PLAIN)
        self.assertEqual(logic.split_nodes_link([node]) , [node])

    def test_split_image_none(self):
        node = TextNode("Just plain text.", TextType.PLAIN)
        self.assertEqual(logic.split_nodes_image([node]) , [node])
    
    def test_split_link_start_end(self):
        node = TextNode("[start](https://a.com) and end [fin](https://b.com)", TextType.PLAIN)
        out = logic.split_nodes_link([node])
        self.assertListEqual( out , [
            TextNode("start", TextType.LINK, "https://a.com"),
            TextNode(" and end ", TextType.PLAIN),
            TextNode("fin", TextType.LINK, "https://b.com"),
        ])
    
    def test_split_image_start_end(self):
        node = TextNode("![one](https://a.png) mid ![two](https://b.png)", TextType.PLAIN)
        out = logic.split_nodes_image([node])
        self.assertListEqual( out , [
            TextNode("one", TextType.IMAGE, "https://a.png"),
            TextNode(" mid ", TextType.PLAIN),
            TextNode("two", TextType.IMAGE, "https://b.png"),
        ])
    def test_split_link_back_to_back(self):
        node = TextNode("[a](u1)[b](u2)", TextType.PLAIN)
        out = logic.split_nodes_link([node])
        self.assertListEqual( out , [
            TextNode("a", TextType.LINK, "u1"),
            TextNode("b", TextType.LINK, "u2"),
        ])

    def test_split_image_back_to_back(self):
        node = TextNode("![a](u1)![b](u2)", TextType.PLAIN)
        out = logic.split_nodes_image([node])
        self.assertListEqual( out , [
            TextNode("a", TextType.IMAGE, "u1"),
            TextNode("b", TextType.IMAGE, "u2"),
        ])

        
    temp = """def test_it_all(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result = logic.text_to_textnodes(text)
        self.assertListEqual(result,[
    TextNode("This is ", TextType.PLAIN),
    TextNode("text", TextType.BOLD),
    TextNode(" with an ", TextType.PLAIN),
    TextNode("italic", TextType.ITALIC),
    TextNode(" word and a ", TextType.PLAIN),
    TextNode("code block", TextType.CODE),
    TextNode(" and an ", TextType.PLAIN),
    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
    TextNode(" and a ", TextType.PLAIN),
    TextNode("link", TextType.LINK, "https://boot.dev"),
])"""

if __name__ == "__main__":
    unittest.main()