import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)


class CheckNone(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold", None)
        self.assertEqual(node, node2)


#class CheckLink(unittest.TestCase):
#    def test_eq(self):
#        node = TextNode("This is a text node", "bold", "www.boot.dev")
#        node2 = TextNode("this is a text node", "bold")
#        self.assertEqual(node, node2)


class PrintNone(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        print(node)


if __name__ == "__main__":
    unittest.main()
