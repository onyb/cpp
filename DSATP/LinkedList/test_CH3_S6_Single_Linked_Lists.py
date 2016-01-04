import unittest

from LinkedList.CH3_S6_Single_Linked_Lists import LinkedList
from LinkedList.CH3_S6_Single_Linked_Lists import Node


class TestSingleLinkedList(unittest.TestCase):
    def test_node(self):
        node_a = Node()
        node_a.set_data('foo')
        self.assertEqual(node_a.get_data(), 'foo')

        node_b = Node()
        node_b.set_data('baz')
        node_a.set_next(node_b)
        self.assertEqual(node_a.get_next(), node_b)

        self.assertEqual(node_a.has_next(), True)
        self.assertEqual(node_b.has_next(), False)

    def test_linked_list(self):
        ll = LinkedList()
        node = Node()
        node.set_data('foo')

        ll.set_head(node)
        self.assertEqual(ll.head, node)
        self.assertEqual(ll.length, 1)

        # Insert at beginning
        ll.insert_at_pos('bar', 0)
        self.assertEqual(ll.head.get_data(), 'bar')
        self.assertEqual(ll.head.get_next().get_data(), 'foo')
        self.assertEqual(ll.length, 2)

        # Insert at end
        ll.insert_at_pos('baz', 2)
        self.assertEqual(ll.head.get_next().get_next().get_data(), 'baz')
        self.assertEqual(ll.length, 3)

        # Insert at position
        ll.insert_at_pos('ani', 1)
        self.assertEqual(ll.head.get_next().get_next().get_data(), 'ani')
        self.assertEqual(ll.length, 4)