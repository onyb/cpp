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
