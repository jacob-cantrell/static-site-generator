import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_no_tag(self):
        leaf1 = LeafNode("p", "Leaf 1")
        leaf2 = LeafNode("p", "Leaf 2")
        node = ParentNode(None, [leaf1, leaf2])
        try:
            node.to_html()
        except ValueError:
            self.assertRaises(ValueError)


    def test_to_html_no_children(self):
        leaf1 = LeafNode("p", "Leaf 1")
        leaf2 = LeafNode("p", "Leaf 2")
        node = ParentNode("h1", None)
        try:
            node.to_html()
        except ValueError:
            self.assertRaises(ValueError)

    def test_to_html_all_leaf_children(self):
        leaf1 = LeafNode("p", "Leaf 1")
        leaf2 = LeafNode("p", "Leaf 2")
        node = ParentNode("h1", [leaf1, leaf2])
        self.assertEqual(
            node.to_html(),
            "<h1><p>Leaf 1</p><p>Leaf 2</p></h1>"
        )

    def test_to_html_all_leaf_w_parent_props(self):
        leaf1 = LeafNode("p", "Leaf 1")
        leaf2 = LeafNode("p", "Leaf 2")
        node = ParentNode("h1", [leaf1, leaf2], {"color": "white"})
        self.assertEqual(
            node.to_html(),
            "<h1 color=\"white\"><p>Leaf 1</p><p>Leaf 2</p></h1>"
        )

    def test_to_html_one_parent_two_levels_no_props(self):
        leaf1 = LeafNode("p", "Leaf 1")
        leaf2 = LeafNode("p", "Leaf 2")
        leaf3 = LeafNode("p", "Leaf 3")
        leaf4 = LeafNode("p", "Leaf 4")
        node2 = ParentNode("h2", [leaf3, leaf4])
        node = ParentNode("h1", [leaf1, node2, leaf2])
        self.assertEqual(
            node.to_html(),
            "<h1><p>Leaf 1</p><h2><p>Leaf 3</p><p>Leaf 4</p></h2><p>Leaf 2</p></h1>"
        )

    def test_to_html_one_parent_two_levels_w_props(self):
        leaf1 = LeafNode("p", "Leaf 1")
        leaf2 = LeafNode("p", "Leaf 2")
        leaf3 = LeafNode("p", "Leaf 3")
        leaf4 = LeafNode("p", "Leaf 4")
        node2 = ParentNode("h2", [leaf3, leaf4], {"color": "white"})
        node = ParentNode("h1", [leaf1, node2, leaf2], {"color": "white"})
        self.assertEqual(
            node.to_html(),
            "<h1 color=\"white\"><p>Leaf 1</p><h2 color=\"white\"><p>Leaf 3</p><p>Leaf 4</p></h2><p>Leaf 2</p></h1>"
        )


    def test_to_html_two_parents_three_levels_no_props(self):
        leaf1 = LeafNode("p", "Leaf 1")
        leaf2 = LeafNode("p", "Leaf 2")
        leaf3 = LeafNode("p", "Leaf 3")
        leaf4 = LeafNode("p", "Leaf 4")
        leaf5 = LeafNode("p", "Leaf 5")
        leaf6 = LeafNode("p", "Leaf 6")
        node3 = ParentNode("h3", [leaf5, leaf6])
        node2 = ParentNode("h2", [leaf3, leaf4, node3])
        node = ParentNode("h1", [leaf1, node2, leaf2])
        self.assertEqual(
            node.to_html(),
            "<h1><p>Leaf 1</p><h2><p>Leaf 3</p><p>Leaf 4</p><h3><p>Leaf 5</p><p>Leaf 6</p></h3></h2><p>Leaf 2</p></h1>"
        )
    
    def test_to_html_two_parents_three_levels_w_props(self):
        leaf1 = LeafNode("p", "Leaf 1")
        leaf2 = LeafNode("p", "Leaf 2")
        leaf3 = LeafNode("p", "Leaf 3")
        leaf4 = LeafNode("p", "Leaf 4")
        leaf5 = LeafNode("p", "Leaf 5")
        leaf6 = LeafNode("p", "Leaf 6")
        node3 = ParentNode("h3", [leaf5, leaf6], {"color": "white"})
        node2 = ParentNode("h2", [leaf3, leaf4, node3], {"color": "white"})
        node = ParentNode("h1", [leaf1, node2, leaf2], {"color": "white"})
        self.assertEqual(
            node.to_html(),
            "<h1 color=\"white\"><p>Leaf 1</p><h2 color=\"white\"><p>Leaf 3</p><p>Leaf 4</p><h3 color=\"white\"><p>Leaf 5</p><p>Leaf 6</p></h3></h2><p>Leaf 2</p></h1>"
        )
