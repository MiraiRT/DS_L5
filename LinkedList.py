class Node:
    def __init__(self, data, next=None):
        self.next = next
        self.data = data

    def __str__(self):
        return self.data


class List:
    def __init__(self, head=None):
        self.head = head
        self.data = head.data
        self.tail = head.next

    def __str__(self):
        s = '['
        if self.isEmpty():
            return '[]'
        else:
            head = self.head
            while True:
                data = head.data
                tail = head.next
                s = s + data + ', '
                if tail == None:
                    return s[0:len(s) - 2] + ']'
                head = tail

    def size(self):
        size = 0
        if self.isEmpty():
            return size
        else:
            head = self.head
            while True:
                head = head.next
                tail = head.next
                size += 1
                if tail == None:
                    size += 1
                    return size

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    def findLast(self):
        head = self.head
        tail = head.next
        while tail != None:
            head = tail
            tail = head.next
        return head

    def append(self, new_data):
        n = Node(new_data)
        if self.isEmpty():
            self.head = n
        else:
            head = self.findLast()
            head.next = n

    def addHead(self, new_data):
        n = Node(new_data, self.head)
        self.head = n
        self.data = n.data
        self.tail = n.next

    def isIn(self, d):
        if self.isEmpty():
            return False
        else:
            head = self.head
            while True:
                data = head.data
                tail = head.next
                if data == d:
                    return True
                if tail == None:
                    return False
                head = tail

    def before(self, d):
        if self.isEmpty() or self.data == d:
            return None
        else:
            head = self.head
            while True:
                tail = head.next
                if tail == None:
                    return None
                if tail.data == d:
                    return head
                head = tail

    def remove(self, d):
        head = self.before(d)  # Before Head
        if head == None:
            return None
        else:
            tail = head.next  # Before Tail
            targetHead = tail  # Target to Remove
            head.next = targetHead.next  # Target Tail to Remove
            return targetHead

    def removeTail(self):
        data = self.findLast().data
        head = self.before(data)
        head.next = None
        return data

    def removeHead(self):
        head = self.head
        self.head = self.head.next
        return head.data

    def reverse(self):
        new_head = self.findLast()
        for i in range(self.size() - 1):
            head = self.findLast()
            tail = self.before(self.findLast().data)
            head.next = tail
            tail.next = None
        self.head = new_head

n3 = Node('C')
n2 = Node('B', n3)
n1 = Node('A', n2)
p = List(n1)
print(p)
p.reverse()
print(p)
