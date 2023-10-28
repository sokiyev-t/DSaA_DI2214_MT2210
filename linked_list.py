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

    def get(self, id):



my_list=LinkedList()
my_list.insert(12)
my_list.insert(15)
my_list.insert(23)
my_list.insert(75)
my_list.insert(1)
print(f"My list len is {my_list.get_counter()}, head is: {my_list.get_element_by_id()}")