class Node:
    def __init__(self, val):
        self.next=None
        self.prev=None
        self.val=val

    def get_prev(self):
        return self.prev

    def set_prev(self, prev):
        self.prev=prev

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next=next

    def get_val(self):
        return self.val

    def set_val(self, val):
        self.val=val

class Queue:
    def __init__(self):
        self.head=None
        self.tail=None

    def push(self, val):
        new_tail=Node(val)
        new_tail.set_prev(self.tail)

        if self.tail:
            self.tail.set_next(new_tail)
        self.tail = new_tail

        if not self.head:
            self.head=new_tail







    def pop(self):
        val=self.head.get_val()
        self.head=self.head.get_next()
        return val

    def is_empty(self):
        return self.head==None

s=Queue()
s.push(5)
s.push(2)
s.push(16)

while not s.is_empty():
    v = s.pop()
    print(v)

