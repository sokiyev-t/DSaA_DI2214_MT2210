import sys
class Node:
    def __init__(self, next=None):
        self.next=next
        self.val=0

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next=next

    def get_val(self):
        return self.val

    def set_val(self, val):
        self.val=val

class LinkedList:
    def __init__(self):
        self.head=None
        self.count=0

    def insert(self, val):
        new_node=Node()
        new_node.set_next(self.head)
        new_node.set_val(val)
        self.head=new_node
        self.count+=1

    def get_counter(self):
        return self.count

    def get_val_by_id(self, id):
        if id<self.count:
            h=self.head
            for i in range(id):
                h=h.get_next()
            return h.get_val()
        else:
           return None

    def insert_by_id(self, id, val):
        if id<self.count:
            h = self.head
            for i in range(id):
                h = h.get_next()
            new_node=Node()
            new_node.set_val(val)
            new_node.set_next(h.get_next())
            h.set_next(new_node)
            self.count+=1
        else:
            return None

    def print_list(self):
        h=self.head
        for i in range(self.count):
            print(h.get_val())
            h=h.get_next()

my_list=LinkedList()
my_list.insert(12)
my_list.insert(15)
my_list.insert(23)
my_list.insert(75)
my_list.insert(1)
my_list.insert_by_id(2,33)
my_list.print_list()

test_node=Node()
test_node.set_val(12)

v=12
s=sys.getsizeof(test_node)
print(f"size of: {s}")

# print(f"My list len is {my_list.get_counter()}, head is: {my_list.head.get_val()}")
#
# v=my_list.get_val_by_id(2)
# print(f"Result is {v}")