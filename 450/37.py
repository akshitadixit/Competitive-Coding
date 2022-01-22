'''
Reverse linked list
'''

from collections import deque
from traceback import print_list


class Node:
    def __init__(self, val=0):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self, vals=[]):
        '''
        l = LinkedList([0, 1, 2, 3, 4])
        '''
        self.head = None
        for x in vals:
            temp = Node(x)
            temp.next = self.head
            self.head = temp

    def reverse(self):
        stack = deque()
        curr = self.head
        while curr != None:
            stack.append(curr.data)

        return LinkedList([stack.pop() for x in range(len(stack))])

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=', ')
            temp = temp.next


vals = [1, 2, 3, 4, 5]
l = LinkedList(vals=vals)
l.printList()
l.reverse().printList()
