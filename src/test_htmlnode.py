import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "hello, world", None, {"href": "https://www.google.com", "target": "_blank"})
        print(node)

if __name__ == "__main__":
    unittest.main()
