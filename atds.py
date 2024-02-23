#!/usr/bin/env python3

"""
atds.py
Advanced Topics Data Structures: Includes a list of multiple python files
"""

__author__ = "William Kim"
__version__ = "2024-02-13"

class Stack():
    """ defines a stack """

    def __init__(self):
        self.stack = []

    def push(self, item):
        """ adds an item onto the stack """
        self.stack.append(item)
    
    def pop(self):
        """ takes out the last item inputted into the stack """
        return self.stack.pop()

    def peek(self):
        """ looks at the last inputted item in the stack """
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None
    
    def size(self):
        """ returns the amount of items in the stack """
        return len(self.stack)
    
    def is_empty(self):
        """ returns true or false if the stack is empty """
        if len(self.stack) == 0:
            return True
        else:
            return False

class Queue():
    """ defines a queue"""

    def __init__(self):
        """Creates the empty list"""
        self.queue = []

    def enqueue(self, item):
        """Adds an item to the back of the queue line"""
        self.queue.append(item)

    def dequeue(self):
        """Takes out the first item in queue and returns that value"""
        return self.queue.pop(0)
    
    def peek(self):
        """Looks at the first item in queue"""
        return self.queue.peek(0)
    
    def size(self):
        """Finds he length of the queue"""
        if len(self.queue) > 0:
            return self.queue[-1]
        else:
            return None
    
    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False
