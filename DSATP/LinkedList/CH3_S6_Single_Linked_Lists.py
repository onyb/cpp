class Node:
    """
    Node of a single linked list
    """

    def __init__(self):
        """
        Constructor for a linked list node
        :return: None
        """
        self.data = None
        self.next = None

    def set_data(self, data):
        """
        Method for setting the data field of the node
        :param data: value to be stored in node
        :return: None
        """
        self.data = data

    def get_data(self):
        """
        Method for getting the data field of the node
        :return: data field of the node
        """
        return self.data

    def set_next(self, next):
        """
        Method for setting the next field of the node
        :param next: reference to the next node
        :return: None
        """
        self.next = next

    def get_next(self):
        """
        Method for getting the next field of the node
        :return: reference to the next node
        """
        return self.next

    def has_next(self):
        """
        Check if node points to another node
        :return: true if node points to another node, false otherwise
        """
        return self.next is not None


class LinkedList:
    """
    Linked list
    """

    def __init__(self):
        """
        Constructor for linked list
        :return: None
        """
        self.head = None

    def set_head(self, node: Node):
        """
            Set head of the linked list to be store an instance of class Node
            :param node: Instance of Node
            :return: None
            """
        self.head = node

    @property
    def length(self):
        """
            Property that returns length of the linked list
            :return: Integer count of the number of nodes in the linked list
            """
        if self.head is None:
            return 0

        current = self.head
        c = 1
        while current.has_next():
            c += 1
            current = current.get_next()
        return c

    def insert_at_beginning(self, data):
        """
        Method for inserting a new node at the beginning of the linked list (head)
        :param data: value to be inserted
        :return: None
        """
        node = Node()
        node.set_data(data)

        if self.length == 0:
            self.head = node
        else:
            node.set_next(self.head)
            self.head = node

    def insert_at_end(self, data):
        """
        Method for inserting a new node at the end of the linked list
        :param data: value to be inserted
        :return: None
        """
        node = Node()
        node.set_data(data)
        node.set_next(None)

        if self.length == 0:
            self.set_head(node)
        else:
            current = self.head
            while current.has_next():
                current = current.get_next()

            current.set_next(node)

    def insert_at_pos(self, data, pos):
        """
        Method for inserting a new node at any position in a linked list
        :param pos: Position where node is to be inserted
        :param data: value to be inserted
        :return: None
        """
        node = Node()
        node.set_data(data)

        if pos > self.length or pos < 0:
            raise InvalidPositionException
        elif pos == 0:
            self.insert_at_beginning(data)
        elif pos == self.length:
            self.insert_at_end(data)
        else:
            current = self.head
            count = 0
            while count < pos:
                current = current.get_next()
                count += 1

            node.set_next(current.get_next())
            current.set_next(node)

    def delete_from_beginning(self):
        """
        Method for deleting a node from the beginning of the linked list
        :return: None
        """
        if self.length == 0:
            raise EmptyListException

        self.head = self.head.get_next()

    def delete_last_node(self):
        """
        Method for deleting a node from the end of the linked list
        :return: None
        """
        if self.length == 0:
            raise EmptyListException

        current = self.head
        previous = None
        while current.has_next():
            previous = current
            current = current.get_next()

        previous.set_next(None)

    def delete_node(self, node):
        if self.length == 0:
            raise EmptyListException

        current = self.head
        previous = self.head
        found = False

        while not found:
            if current == node:
                found = True

            elif current is None:
                # Reached end of linked list
                raise ElementNotFoundException
            else:
                previous = current
                current = current.get_next()

        if previous is self.head:
            # The item to be deleted is the head
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def delete_value(self, value):
        """
        Method to delete a node from a linked list with a particular value
        :param value: data value of the node to be matched with
        :return: None
        """
        if self.length == 0:
            raise EmptyListException

        current = self.head
        previous = self.head
        found = False

        while not found:
            if current.get_data() == value:
                found = True

            elif current is None:
                # Reached end of linked list
                raise ElementNotFoundException
            else:
                previous = current
                current = current.get_next()

        if previous is self.head:
            # The item to be deleted is the head
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def delete_pos(self, pos):
        """
        Method to delete a node from a linked list at a given position
        :param pos: Index of node to be deleted
        :return: None
        """
        if self.length == 0:
            raise EmptyListException

        count = 0
        current = self.head
        previous = self.head

        if pos > self.length or pos < 0:
            raise InvalidPositionException

        while count < pos:
            count += 1
            previous = current
            current = current.get_next()

        previous.set_next(current.get_next())

    def clear(self):
        """
        Remove linked list from memory
        :return: None
        """
        self.head = None


class InvalidPositionException(Exception):
    pass


class EmptyListException(Exception):
    pass


class ElementNotFoundException(Exception):
    pass
