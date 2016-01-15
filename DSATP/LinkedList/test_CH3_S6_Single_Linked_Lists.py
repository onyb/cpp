import unittest

from LinkedList.CH3_S6_Single_Linked_Lists import LinkedList
from LinkedList.CH3_S6_Single_Linked_Lists import Node
from LinkedList.CH3_S6_Single_Linked_Lists import ElementNotFoundException


class TestSingleLinkedList(unittest.TestCase):
    def test_node(self):
        node_a = Node()
        node_a.set_data('foo')
        self.assertEqual(node_a.get_data(), 'foo')

        node_b = Node()
        node_b.set_data('baz')
        node_a.set_next(node_b)
        self.assertEqual(node_a.get_next(), node_b)

        self.assertEqual(node_a.has_next, True)
        self.assertEqual(node_b.has_next, False)

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

        # Delete from beginning
        ll.delete_from_beginning()
        self.assertEqual(ll.head.get_data(), 'foo')
        self.assertEqual(ll.length, 3)

        # Delete last node
        ll.delete_last_node()
        self.assertEqual(ll.head.get_next().get_data(), 'ani')
        self.assertEqual(ll.head.get_next().get_next(), None)
        self.assertEqual(ll.length, 2)

        # Delete node
        ll.insert_at_pos('anirudha', 2)
        ll.insert_at_pos('bose', 3)
        self.assertEqual(ll.length, 4)
        node = ll.head.get_next().get_next()
        ll.delete_node(node)
        self.assertEqual(ll.length, 3)

        # Delete a non-existent node
        node = Node()
        node.set_data('pirated')
        with self.assertRaises(ElementNotFoundException):
            ll.delete_node(node)
        self.assertEqual(ll.length, 3)

        # Delete value
        ll.insert_at_pos('onyb', 2)
        self.assertEqual(ll.head.get_next().get_next().get_next().get_data(), 'onyb')
        self.assertEqual(ll.length, 4)
        ll.delete_value('onyb')
        self.assertEqual(ll.head.get_next().get_data(), 'ani')
        self.assertEqual(ll.length, 3)

        # Delete position
        ll.insert_at_pos('onyb', 2)
        self.assertEqual(ll.head.get_next().get_next().get_next().get_data(), 'onyb')
        self.assertEqual(ll.length, 4)
        ll.delete_pos(2)
        self.assertEqual(ll.head.get_next().get_data(), 'ani')
        self.assertEqual(ll.length, 3)

        # Clear linked list
        ll.clear()
        self.assertEqual(ll.length, 0)