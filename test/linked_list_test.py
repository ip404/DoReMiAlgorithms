#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import sys
import unittest
sys.path.append("..")

from Code.data_structures.linear_list.linked_list import SinglyLinkedList


class SinglyLinkedListTestCase(unittest.TestCase):

    def setUp(self):
        print('\n-----------------------------setUp')

    # def tearDown(self):
    #     print('tearDown')
    @staticmethod
    def test_insert_element_at_index():
        singly_list = SinglyLinkedList(name='singly list insert')
        singly_list.print_all_element()
        # singly_list.insert_element_at_index('a', 10)
        # singly_list.print_all_element()
        singly_list.insert_element_at_index('a', 0)
        singly_list.print_all_element()
        singly_list.insert_element_at_index('b', 0)
        singly_list.print_all_element()
        singly_list.insert_element_at_index('c', 1)
        singly_list.print_all_element()
        singly_list.insert_element_at_index('d', 2)
        singly_list.print_all_element()

    @staticmethod
    def test_append_element():
        singly_list = SinglyLinkedList(name='singly list append')
        singly_list.print_all_element()
        singly_list.append_element('a')
        singly_list.print_all_element()
        singly_list.append_element('c')
        singly_list.print_all_element()
        singly_list.append_element('b')
        singly_list.print_all_element()
        singly_list.append_element('f')
        singly_list.print_all_element()

    @staticmethod
    def test_remove_element_at_index():
        singly_list_a = SinglyLinkedList(name='singly list remove first')
        singly_list_a.append_element('j')
        singly_list_a.append_element('k')
        singly_list_a.append_element('l')
        singly_list_a.remove_element_at_index(0)
        singly_list_a.print_all_element()

        singly_list_b = SinglyLinkedList(name='singly list remove')
        singly_list_b.append_element('j')
        singly_list_b.append_element('k')
        singly_list_b.append_element('l')
        singly_list_b.remove_element_at_index(1)
        singly_list_b.print_all_element()

        singly_list_c = SinglyLinkedList(name='singly list remove last')
        singly_list_c.append_element('j')
        singly_list_c.append_element('k')
        singly_list_c.append_element('l')
        singly_list_c.remove_element_at_index(2)
        singly_list_c.print_all_element()

    @staticmethod
    def test_update_element_at_index():
        singly_list = SinglyLinkedList(name='singly list update')
        singly_list.append_element('e')
        singly_list.append_element('t')
        singly_list.append_element('a')
        singly_list.update_element_at_index('d', 2)
        singly_list.print_all_element()
        singly_list.update_element_at_index('u', 0)
        singly_list.print_all_element()
        singly_list.update_element_at_index('p', 1)
        singly_list.print_all_element()

    @staticmethod
    def test_last():
        singly_list = SinglyLinkedList(name='singly list get last')
        print(singly_list.last())
        singly_list.append_element('l')
        print(singly_list.last())
        singly_list.append_element('a')
        singly_list.append_element('s')
        print(singly_list.last())

    # @staticmethod
    # def test_element_at_index():
    #     singly_list = SinglyLinkedList(name='singly list get')
    #     print(singly_list.element_at_index(0))
    #     singly_list.append_element('g')
    #     singly_list.append_element('e')
    #     singly_list.append_element('t')
    #     singly_list.element_at_index(0)
    #     singly_list.element_at_index(1)
    #     singly_list.element_at_index(2)
    #     singly_list.element_at_index(3)


if __name__ == "__main__":
    unittest.main()