#!/usr/bin/env python
# -*- coding:utf-8 -*-

import abc

class AbstractQueue(abc.ABC):
    pass


class LinkedQueue(AbstractQueue):
    def __init(self, name):
        pass

    def enqueue(self):
        pass
    
    def dequeue(self):
        pass
    
    def length(self):
        pass
    
    def is_empty(self):
        pass

if __name__ == "__main__":
    print('queue main')
