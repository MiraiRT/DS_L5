# Scramble Without Python List ! #
class Node:
    def __init__(self, data, next=None):
        self.next = next
        self.data = data

    def __str__(self):
        return self.data


class List:
    def __init__(self, head=None):
        self.head = head

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
            self.head.next = None
        else:
            head = self.findLast()
            head.next = n

    def bottomUp(self, p):  # Shuffle Data
        n = int(self.size() * (int(p) / 100))
        print('Shuffle')
        h1 = self.head
        head = h1
        for i in range(n - 1):
            t1 = head.next
            head = t1
        h2 = head.next
        t2 = self.findLast()
        t1.next = None
        t2.next = h1
        self.head = h2
        print(self)

    def deBottomUp(self, p):  # Shuffle Data Back
        n = self.size() - int((self.size() * (int(p) / 100)))
        print('Shuffle Back')
        h1 = self.head
        head = h1
        for i in range(n - 1):
            t1 = head.next
            head = t1
        h2 = head.next
        t2 = self.findLast()
        t1.next = None
        t2.next = h1
        self.head = h2
        print(self)

    def riffle(self, p):
        n = int(self.size() * (int(p) / 100))
        print('Riffle')
        h1 = self.head
        head = h1
        for i in range(n - 1):
            t1 = head.next
            head = t1
        h2 = head.next
        t1.next = None
        i = 1
        while True:
            if i % 2 != 0:
                head = h1
                h1 = h1.next
                head.next = h2
            else:
                head = h2
                h2 = h2.next
                head.next = h1
            if h1.next == None:
                head = h2
                h2 = h2.next
                head.next = h1
                h1.next = h2
                break
            if h2.next == None:
                head = h1
                h1 = h1.next
                head.next = h2
                h2.next = h1
                break
            i += 1
        print(self)

    def deRiffle(self, p):
        n = self.size() - int(self.size() * (int(p) / 100))
        print('Riffle Back')
        head = self.head
        h1 = head
        h2, tmp = head.next, head.next
        if n > int(self.size() / 2):
            n = int(self.size() * (int(p) / 100))
            for i in range(n - 1):
                head = h2.next
                ref1, ref2 = head, head.next
                h1.next = ref1
                h2.next = ref2
            ref1.next = tmp
        else:
            for i in range(n - 1):
                head = h2.next
                ref1, ref2 = head, head.next
                h1.next = ref1
                h2.next = ref2
            ref1.next = ref2.next
            ref2.next = None
            head = self.head
            for i in range(self.size() - 1):
                head = head.next
            head.next = tmp
        print(self)


def createNumber(n):
    l = List()
    for i in range(n):
        l.append(str(i + 1))
    print(l)
    return l


l = createNumber(6)
p1 = 40
l.bottomUp(p1)
l.deBottomUp(p1)
l.riffle(p1)
l.deRiffle(p1)
