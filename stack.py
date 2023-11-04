class Node:
    def __init__(self, val):
        self.next=None
        self.val=val

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next=next

    def get_val(self):
        return self.val

    def set_val(self, val):
        self.val=val

class Stack:
    def __init__(self):
        self.head=None

    def push(self, val):
        new_head=Node(val)
        new_head.set_next(self.head)
        self.head=new_head

    def pop(self):
        val=self.head.get_val()
        self.head=self.head.get_next()
        return val

    def is_empty(self):
        return self.head==None

s=Stack()
s.push(5)
s.push(2)
s.push(16)

while not s.is_empty():
    v = s.pop()
    print(v)

# v=s.pop()
# print(v)
# v=s.pop()
# print(v)