import unittest
from debug_utils import *
from blocks import block_to_blocktype, BlockType

class TestBlocks(unittest.TestCase):

    def test_biggest_heading(self):
        input = "# Testing"
        output = block_to_blocktype(input)
        self.assertEqual(output, BlockType.HEADING)

    def test_smallest_heading(self):
        input = "###### Testing"
        output = block_to_blocktype(input)
        self.assertEqual(output, BlockType.HEADING)

    def test_broken_heading(self):
        input = "## test \n testing"
        output = block_to_blocktype(input)
        self.assertEqual(output, BlockType.PARAGRAPH)

    def test_code_generic(self):
        input = """```
 def test_code_specified(self):
        pass
```"""
        output = block_to_blocktype(input)
        self.assertEqual(output, BlockType.CODE)

    def test_code_specified(self):
        input = """```py
 def test_code_specified(self):
        pass
```"""
        output = block_to_blocktype(input)
        self.assertEqual(output, BlockType.CODE)

    def test_quote(self):
        input = """> hi
> hello"""
        output = block_to_blocktype(input)
        self.assertEqual(output, BlockType.QUOTE)

    def test_broken_quote(self):
        input = """> hi
test
> hello"""
        output = block_to_blocktype(input)
        self.assertEqual(output, BlockType.PARAGRAPH)

    def test_unordered_list(self):
        input = """- hi
- test
- hello"""
        output = block_to_blocktype(input)
        self.assertEqual(output, BlockType.UNORDERED_LIST)

    def test_broken_unordered_lits(self):
        input = """- hi
 test
- hello"""
        output = block_to_blocktype(input)
        self.assertEqual(output, BlockType.PARAGRAPH)

    def test_ordered_list(self):
        input = """1. hi
2. test
3. hello"""
        output = block_to_blocktype(input)
        self.assertEqual(output, BlockType.ORDERED_LIST)

    def test_broken_ordered_list(self):
        input = """1. hi
 test
3. hello"""
        output = block_to_blocktype(input)
        self.assertEqual(output, BlockType.PARAGRAPH)

    def test_paragraph(self):
        input = """just text
more text"""
        output = block_to_blocktype(input)
        self.assertEqual(output, BlockType.PARAGRAPH)