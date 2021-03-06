#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .linear_list import AbstractLinearList


class SinglyLinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        self_id = 0
        if self is not None:
            self_id = id(self)
        self_next_id = 0
        if self.next is not None:
            self_next_id = id(self.next)
        return "\nself:{0}_value:{1}_next:{2}".format(self_id, self.value, self_next_id)

    def __repr__(self):
        return self.__str__()


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

    def insert_element_at_index(self, element, index):
        """
        list[index].value = element
        list[index].next = original element at index
        :param element:
        :param index:
        :return:
        """
        if index > self.length():
            raise Exception('index out of singly list range')
        else:
            temp_index = 0
            next_node = self.header_node.next
            previous_node = self.header_node
            while (temp_index < index) and (next_node is not None):
                temp_index += 1
                previous_node = next_node
                next_node = next_node.next
            node = SinglyLinkedListNode(element)
            previous_node.next = node
            node.next = next_node
            self.header_node.value += 1

    def append_element(self, element):
        self.insert_element_at_index(element, self.length())

    def remove_element_at_index(self, index):
        if index >= self.length():
            raise Exception('index out of singly list range')
        else:
            temp_index = 0
            next_node = self.header_node.next
            previous_node = self.header_node
            while temp_index < index:
                temp_index += 1
                previous_node = next_node
                next_node = next_node.next
            delete_node = next_node
            previous_node.next = delete_node.next
            # del delete_node
            self.header_node.value -= 1

    def remove_all_element(self):
        self.header_node.next = None
        self.header_node.value = 0

    def update_element_at_index(self, element, index):
        if index >= self.length():
            raise Exception('index out of singly list range')
        else:
            temp_index = 0
            next_node = self.header_node.next
            while temp_index < index:
                temp_index += 1
                next_node = next_node.next
            next_node.value = element

    def first(self):
        return self.header_node.next.value

    def last(self):
        if self.length() == 0:
            return None
        else:
            next_node = self.header_node.next
            while next_node.next is not None:
                next_node = next_node.next
            return next_node.value

    def element_at_index(self, index):
        if index >= self.length():
            raise Exception('index out of singly list range')
        else:
            temp_index = 0
            next_node = self.header_node.next
            while temp_index < index:
                temp_index += 1
                next_node = next_node.next
            return next_node.value

    def index_of_element(self, element):
        if element is None:
            # not exist
            return -1
        temp_index = 0
        next_node = self.header_node
        while next_node.next is not None:
            next_node = next_node.next
            if next_node.value is element:
                return temp_index
            temp_index += 1
        return -1

    def length(self):
        return self.header_node.value

    def print_all_element(self):
        next_node = self.header_node.next
        element_list = []
        while next_node is not None:
            element_list.append(next_node)
            next_node = next_node.next
        print('{0}---------------\n {1}'.format(self.name, element_list))
        # del element_list


class DoublyLinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None

    def __str__(self):
        previous_id = 0
        if self.previous is not None:
            previous_id = id(self.previous)
        self_id = 0
        if self is not None:
            self_id = id(self)
        next_id = 0
        if self.next is not None:
            next_id = id(self.next)
        return "\nprevious:{0}_self:{1}_value:{2}_next:{3}".format(previous_id, self_id, self.value, next_id)

    def __repr__(self):
        return self.__str__()


class DoublyLinkedList(AbstractLinearList):
    # TODO
    pass

if __name__ == '__main__':
    print('run linked_list.py')

__all__ = ["SinglyLinkedListNode", "SinglyLinkedList", "DoublyLinkedListNode", "DoublyLinkedList"]

# class AbstractLinkedList(AbstractLinearList):
