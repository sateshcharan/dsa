class Node:
    def __init__ (self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__ (self):
        self.head = self.tail = None

    def insert_at_begining(self, data):
        node = Node(data)
        if self.head is None:
            self.head = self.tail = Node(data)
            return
        self.head.prev = node
        node.next = self.head
        self.head = node

    def insert_at_end(self, data):
        if self.tail is None:
            self.head = self.tail = Node(data)
            return
        node = Node(data, None, self.tail)
        self.tail.next = node
        self.tail = node

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            print("invalid index")
            return
        itr = self.head
        count = 0
        node = Node(data)
        while itr.next:
            if count == index - 1:
                node.prev = itr
                node.next = itr.next
                itr.next.prev = node
                itr.next = node
                return
            itr = itr.next
            count += 1
    
    def insert_value(self, data_list):
        self.head = self.tail = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            print('the list is empty')
            return
        index = self.get_index(data_after)
        if index > 0:
            self.insert_at(index + 1, data_to_insert)
        
    def remove_at_begining(self):
        if self.head is None:
            print('the list is empty')
        itr = self.head
        self.head = itr.next
        self.head.prev = None
   
    def remove_at_end(self):
        if self.tail is None:
            print('the list is empty')
        self.tail = self.tail.prev
        self.tail.next = None

    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            print("invalid index")
            return
        if index == 0:
            self.remove_at_begining()
            return
        if index == self.get_length():
            self.remove_at_end()
        itr = self.head
        count = 0
        while itr:
            if count == index:
                itr.next.prev = itr.prev
                itr.prev.next = itr.next
                return
            itr = itr.next
            count += 1

    def remove_by_value(self, value):
        index = self.get_index(value)
        if index < 0:
            print("value not found")
            return
        if index == self.get_length() - 1:
            self.remove_at_end()
            return
        self.remove_at(index)

    def get_index(self, val):
        if self.head is None:
            return -1
        itr = self.head
        count = 0
        while itr:
            if itr.data == val:
                return count
            itr = itr.next
            count += 1
        return -1

    def get_length(self):
        if self.head is None:
            return -1
        itr = self.head
        count = 0
        while itr:
            itr = itr.next
            count += 1
        return count

    def print_forward(self):
        if self.head is None:
            print("the list is empty")
            return
        itr = self.head
        dlst = ""
        while itr:
            dlst += str(itr.data) + '<->'
            itr = itr.next
        print(dlst)

    def print_backward(self):
        if self.tail is None:
            print("the list is empty")
            return
        itr = self.tail
        dlst = ""
        while itr:
            dlst += str(itr.data) + '<->'
            itr = itr.prev
        print(dlst)

dllist = DoublyLinkedList()
dllist.insert_at_begining(100)
dllist.insert_at_begining(200)
dllist.insert_at_end(300)
dllist.insert_at(1,400)
dllist.insert_value([1,2,3,4,5])
dllist.insert_after_value(3,300)
dllist.remove_at_begining()
dllist.remove_at_end()
dllist.remove_at(2)
dllist.remove_by_value(4)
dllist.print_forward()
dllist.print_backward()