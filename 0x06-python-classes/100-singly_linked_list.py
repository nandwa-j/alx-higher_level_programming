#!/usr/bin/python3
""" Node module """


class Node:
    """ Declares the class """

    def __init__(self, data, next_node=None):
        """
        Initializes the attributes of node class

        Args:
            data: value of node
            next_node: address of next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Gets data of a linked list """
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ Declares a class of a singlyLinkedList """
    def __str__(self):
        rtn = ""
        p = self.__head

        while p is not None:
            rtn += str(p.data)
            if p.next_node is not None:
                rtn += "\n"
            p = p.next_node

        return rtn

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """
        sorts the node values

        Args:
        value: value of node
        """
        p = self.__head

        while p is not None:
            if p.data > value:
                break
            p_prev = p
            p = p.next_node

        newNode = Node(value, p)
        if p == self.__head:
            self.__head = newNode
        else:
            p_prev.next_node = newNode
