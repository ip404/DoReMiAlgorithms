#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .linear_list import AbstractLinearList


class SinglyLinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return "\nself:{0}-value:{1}-next:{2}".format(id(self), self.value, id(self.next))

    def __repr__(self):
        return "\nself:{0}-value:{1}-next:{2}".format(id(self), self.value, id(self.next))


class SinglyLinkedList(AbstractLinearList):
    def __init__(self, name, circular=False):
        super(SinglyLinkedList, self).__init__(name)
        # use header_node.value to save the length of list
        # use header_node.next to save the first node of list
        self.header_node = SinglyLinkedListNode(0)
        # TODO
        self.is_circular = circular

    def __str__(self):
        return "name {0}, circular: {1}".format(self.name, self.is_circular)

    def append_element(self, element):
        self.insert_element_at_index(element, self.length())

    def insert_element_at_index(self, element, index):
        """
        list[index].value = element
        list[index].next = original element at index
        :param element:
        :param index:
        :return:
        """
        if index > self.length():
            raise Exception('out of list range')
        else:
            temp_index = 0
            next_node = self.header_node.next
            previous_node = self.header_node
            while (temp_index < index) and (next_node is not None):
                print('---------')
                temp_index += 1
                previous_node = next_node
                next_node = next_node.next
            node = SinglyLinkedListNode(element)
            previous_node.next = node
            node.next = next_node
            self.header_node.value += 1

    def remove_element_at_index(self, index):
        if index == 0:
            pass
        elif index > self.length():
            pass
        else:
            pass
        temp_index = 0
        next_node = self.header_node.next
        while temp_index < index:
            temp_index += 1
            next_node = next_node.next
        delete_node = next_node.next
        next_node.next = delete_node.next
        # del delete_node
        self.header_node.value -= 1

    def remove_all_element(self):
        self.header_node.next = None
        self.header_node.value = 0

    def update_element_at_index(self, element, index):
        pass

    def first(self):
        return self.header_node.next.value

    def last(self):
        pass

    def element_at_index(self, index):
        pass

    def index_of_element(self, element):
        pass

    def length(self):
        return self.header_node.value

    def print_all_element(self):
        next_node = self.header_node.next
        element_list = []
        while next_node is not None:
            element_list.append(next_node)
            next_node = next_node.next
        print(element_list)
        del element_list


class DoublyLinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None


class DoublyLinkedList(AbstractLinearList):
    pass

if __name__ == '__main__':
    print('run linked_list.py')

__all__ = ["SinglyLinkedListNode", "SinglyLinkedList", "DoublyLinkedListNode", "DoublyLinkedList"]

# class AbstractLinkedList(AbstractLinearList):
