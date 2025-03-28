import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        test_dict = {
            "href": "https://www.google.com",
            "target": "_blank"
        }
        node = HTMLNode("p", "value text", None, test_dict)
        node2 = HTMLNode("p", "value text", None, test_dict)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        test_dict = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode("p", "value text", None, test_dict)
        node2 = HTMLNode("h1", "value text", None, test_dict)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()