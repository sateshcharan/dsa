class Node:
    def __init__ (self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__ (self):
        self.head = None

    def insert_at_begining(self, data):
        self.head = Node(data, self.head)

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            print("invalid index")
            return
        if self.head is None:
            self.insert_at_begining(data)
            return
        itr = self.head
        count = 0
        while itr:
            if count == index -1:
                itr.next = Node(data, itr.next)
                return
            itr = itr.next
            count += 1

    def insert_at_end(self, data):
        index = self.get_length()
        self.insert_at(index, data)

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            print("the list is empty cannot insert after value")
            return
        index = self.get_index(data_after) + 1
        self.insert_at(index, data_to_insert)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def remove_at_begining(self):
        if self.head is None:
            print("the list is empty cannot remove at begining")
            return
        self.head = self.head.next

    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            print("invalid index cannot remove")
        if self.head is None:
            print("the list is empty cannot remove at index")
            return
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                return
            itr = itr.next
            count += 1

    def remove_at_end(self):
        index = self.get_length() - 1
        self.remove_at(index)

    def remove_by_value(self, value):
        index = self.get_index(value)
        if index < 0:
            print("invalid value")
            return
        self.remove_at(index)

    def get_index(self, value):
        if self.head is None:
            print('the list is empty cannot get index')
            return
        itr = self.head
        count = 0
        while itr:
            if itr.data == value:
                return count
            itr = itr.next
            count += 1

    def get_length(self):
        if self.head is None:
            return 0
        itr = self.head
        count = 0
        while itr:
            itr = itr.next
            count += 1
        return count

    def print_list(self):
        if self.head is None:
            print("the list is empty cannot print list")
            return
        itr = self.head
        lst = ""
        while itr:
            lst += str(itr.data) + "-->"
            itr = itr.next        
        print(lst)          

llist = LinkedList()
llist.insert_at_begining(100)
llist.insert_at_begining(200)
llist.insert_at_begining(300)
llist.insert_at(0, 400)
llist.insert_at_end(500)
llist.insert_values([100,200,300,400,500])
llist.insert_after_value(300, 30)
llist.remove_at_begining()
llist.remove_at(2)
llist.remove_at_end()
llist.remove_by_value(300)
llist.print_list()