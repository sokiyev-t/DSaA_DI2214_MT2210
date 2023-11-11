class Node:
    def __init__(self, val):
        self.next=None
        self.prev=None
        self.val=val

class Deq:
    def __init__(self):
        self.head=None
        self.tail=None


    def push_front(self, val):
        new_head=Node(val)
        new_head.next=self.head

        if self.head:
            self.head.prev=new_head

        self.head = new_head

        if not self.tail:
            self.tail=new_head


    def push_back(self, val):
        new_tail=Node(val)
        new_tail.prev=self.tail

        if self.tail:
            self.tail.next=new_tail
        self.tail = new_tail

        if not self.head:
            self.head=new_tail

    def pop_front(self):
        val=self.head.val
        self.head=self.head.next
        return val

    def pop_back(self):
        val=self.tail.val
        self.tail=self.tail.prev
        return val

    def is_empty(self):
        return self.head==None or self.tail==None


s=Deq()
s.push_back(5)
s.push_back(6)
s.push_back(8)
s.push_back(9)
s.push_front(15)

while not s.is_empty():
    v = s.pop_front()
    print(v)

