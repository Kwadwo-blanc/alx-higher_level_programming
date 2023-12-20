#!/usr/bin/python3

"""Define classes for a singly-linked list."""


class Node:
     """Represent a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """
        Initializes a new Node class.

        Args:
        data (int): The data to be stored in the node.
        next_node (Node, optional): The next node in the linked list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the data stored in the node."""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
            self.__data = value

    @property
    def next_node(self):
        """Retrieves the next node in the linked list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
            self.__next_node = value


class SinglyLinkedList:
    """This class defines a singly linked list."""

    def __init__(self):
        """Initializes a new SinglyLinkedList class."""
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the sign linked list.

        Args:
        - value (int): The value to be inserted into the list.
        """                                                                                                                                                                                                                         
        new_node = Node(value)

        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and
            current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.rstrip()
