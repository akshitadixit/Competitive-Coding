'''
- add 1 to a number represented as a linked list
- add 2 numbers represented as linked lists
'''


from numpy import insert


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
        pos = self.len + pos + 1 if pos < 0 else pos
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

    def add1(self, x=1):
        curr = self.head.next
        carry = x  # cz we have to add 1
        while curr != None and carry > 0:
            sum = curr.data + carry
            curr.data = sum % 10
            carry = sum//10
            curr = curr.next
        if carry != 0:
            self.insert(carry, -1)

    def add2(self, ll):
        curr1 = self.head.next
        curr2 = ll.head.next
        l1, l2 = self.len, ll.len
        sum, carry = 0, 0
        if l1 < l2:
            # first list will be added to second
            curr1, curr2 = curr2, curr1

        while curr1 != None:
            sum = curr1.data + curr2.data + carry
            curr1.data = sum % 10
            carry = sum//10
            curr1 = curr1.next
            curr2 = curr2.next
        while curr2 != None and carry > 0:
            sum = curr2.data + carry
            curr2.data = sum % 10
            carry = sum//10
            curr2 = curr2.next
        if carry != 0:
            curr2.insert(carry, -1)

        return curr2


arr = [9, 9, 9, 9]
arr2 = [1, 1, 1]
ll = LinkedList()
for x in arr:
    ll.insert(x)

ll.print()
ll.add1()
ll.print()

ll1 = LinkedList()
for x in arr2:
    ll1.insert(x)

ll1.print()
ll2 = ll.add2(ll1)
ll2.print()
