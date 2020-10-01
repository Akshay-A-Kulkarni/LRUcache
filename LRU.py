"""
LRU.py

My scratch implementation of an LRU cache
-----------------------------------------------------------------------------
 Author: Akshay Kulkarni -- Date: 10/2020
-----------------------------------------------------------------------------

"""


class Node:
    def __init__(self, key, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, cap):
        self.capacity = cap
        self.nodemap = {}
        self.head = Node('H')
        self.tail = Node('T')
        self.head.next = self.tail
        self.tail.prev = self.head

    def put(self, key, value):
        if key in self.nodemap:
            self.nodemap[key].val = value
            self.__remove(self.nodemap[key])
            self.__insert(self.nodemap[key])
        else:
            if len(self.nodemap) != self.capacity:
                self.nodemap[key] = Node(key, value)
                self.__insert(self.nodemap[key])
            else:
                self.__remove(self.tail.prev)
                self.nodemap[key] = Node(key, value)
                self.__insert(self.nodemap[key])

    def get(self, key):
        if key in self.nodemap:
            node = self.nodemap[key]
            self.__remove(node)
            self.__insert(node)
            return node
        else:
            raise KeyError('Key does not exist in this LRU cache')

    def __remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def __insert(self, New_Node):

        old_head_next = self.head.next
        self.head.next = New_Node
        old_head_next.prev = New_Node
        New_Node.prev = self.head
        New_Node.next = old_head_next

    def __str__(self):
        node = self.head.next
        string = ''
        while node.next != None:
            if node.next.next is None:
                string += str(node.val)
            else:
                string += str(node.val) + '=>'
            node = node.next
        return string
