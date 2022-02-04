'''
reverse a linked list in groups of 'k' elements
'''

class Node:
    def __init__(self, val=0):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()
        self.len = 0

    def insert(self, val, pos=0):
        curr = self.head
        pos = self.len + pos if pos < 0 else pos
        while pos > 0:
            pos -= 1
            curr = curr.next

        node = Node(val)
        node.next = curr.next
        curr.next = node
        self.len += 1

    def delete(self, pos=0):
        prev = self.head
        curr = prev.next
        pos = self.len + pos if pos < 0 else pos
        while pos > 0:
            pos -= 1
            prev = curr
            curr = curr.next
        prev.next = curr.next
        curr.next = None
        self.len -= 1

    def print(self):
        curr = self.head.next
        while curr != None:
            print(curr.data, end=' ')
            curr = curr.next
        print()

    def reverse(self, head, k):
        ctr = 0
        curr = head
        next = None
        prev = None
        while curr != None and ctr < k:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            ctr += 1
        if next != None:
            head.next = self.reverse(next, k)

        return prev


arr = [1, 2, 3, 4, 5, 6]
ll = LinkedList()
for x in arr:
    ll.insert(x)

ll.print()
ll.head = ll.reverse(ll.head.next, 4)
ll.print()
