#!/usr/bin/env python
# -*- coding:utf-8 -*-

from abc import ABC
from abc import abstractclassmethod


class AbstractLinearList(ABC):
    def __init__(self, name):
        self.name = name

    def __len__(self):
        return self.length()

    @abstractclassmethod
    def insert_element_at_index(self, element, index):
        pass

    @abstractclassmethod
    def append_element(self, element):
        pass

    @abstractclassmethod
    def remove_element_at_index(self, index):
        pass

    @abstractclassmethod
    def remove_all_element(self):
        pass

    @abstractclassmethod
    def update_element_at_index(self, element, index):
        pass

    @abstractclassmethod
    def first(self):
        pass

    @abstractclassmethod
    def last(self):
        pass

    @abstractclassmethod
    def element_at_index(self, index):
        pass

    @abstractclassmethod
    def index_of_element(self, element):
        pass

    @abstractclassmethod
    def length(self):
        pass

    def is_empty(self):
        False if self.length() > 0 else True


if __name__ == "__main__":
    pass
