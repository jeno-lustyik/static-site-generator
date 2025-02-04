import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        props = {
            "href": "http://nyomod.fasz",
            "target": "_blank",
        }
        node = HTMLNode(props=props)
        self.assertEqual(' href="http://nyomod.fasz" target="_blank"', node.props_to_html())

    def test_props_to_html_false(self):
        props = {
            "href": "http://nyomod.fasz",
            "target": "",
        }
        node = HTMLNode(props=props)
        self.assertNotEqual(' href="http://nyomod.fasz" target="_blank"', node.props_to_html())


    def test_repr(self):
        node = HTMLNode("1", "2", "3", "4")
        self.assertEqual(repr(node), 'HTMLNode(1, 2, 3, 4)')

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("a", "vegig vagyunk", {"href": "nyomod.com"})
        self.assertEqual(node.to_html(), '<a href="nyomod.com">vegig vagyunk</a>')


    def test_to_html_noprops(self):
        node = LeafNode("p", "vegig vagyunk")
        self.assertEqual(node.to_html(), '<p>vegig vagyunk</p>')

    def test_to_html_novalue(self):
        node = LeafNode("b", value=None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_notag(self):
        node = LeafNode(None, "nyomjuk")
        self.assertEqual(node.to_html(), "nyomjuk")


class TestParentNode(unittest.TestCase):
    def test_to_html1(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), expected)
