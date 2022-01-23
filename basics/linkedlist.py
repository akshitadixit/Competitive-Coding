class Node:
    def __init__(self, val=0):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()
        self.len = 0

    def insert(self, val, k=0):
        curr = self.head
        k = self.len + k if k < 0 else k
        node = Node(val)
        while k > 0:
            k -= 1
            curr = curr.next

        node.next = curr.next
        curr.next = node
        self.len += 1

    def delete(self, k=0):
        prev = self.head
        curr = prev.next
        k = self.len - k if k < 0 else k
        while k > 0:
            k -= 1
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

# driver


arr = [1, 2, 3, 4, 5, 6, 7]
ll = LinkedList()
for x in arr:
    ll.insert(x)
ll.print()
ll.delete(3)
ll.insert(234, -2)
ll.print()