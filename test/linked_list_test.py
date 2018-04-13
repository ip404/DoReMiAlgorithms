#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import sys
import unittest
sys.path.append("..")

from Code.data_structures.linear_list.linked_list import SinglyLinkedList


class SinglyLinkedListTestCase(unittest.TestCase):

    def setUp(self):
        print('-----------------------------setUp')

    # def tearDown(self):
    #     print('tearDown')
    @staticmethod
    def test_insert_element_at_index():
        singly_list = SinglyLinkedList(name='singly list')
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
        singly_list = SinglyLinkedList(name='singly list')
        singly_list.print_all_element()
        singly_list.append_element('a')
        singly_list.print_all_element()
        singly_list.append_element('c')
        singly_list.print_all_element()
        singly_list.append_element('b')
        singly_list.print_all_element()
        singly_list.append_element('f')
        singly_list.print_all_element()


if __name__ == "__main__":
    unittest.main()