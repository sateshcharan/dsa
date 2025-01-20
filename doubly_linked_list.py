class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class doubly_linked_list:
    def __init__(self):
        self.head = self.tail = None

    def insert_at_begining(self, data):
        node = Node(data)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

    def insert_at_end(self, data):
        node = Node(data)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
    
    def insert_at(self, index, data):
        if index < 0 or index > self.get_length() - 1:
            print("invalid index")

        if self.head is None:
            print("the list is empty")

        node = Node(data)
        itr = self.head
        count = 0
        while itr.next:
            if count == index - 1 :
                node.prev = itr
                node.next = itr.next
                node.next.prev = node
                itr.next = node
                return
            itr = itr.next
            count += 1

    def insert_values(self, data_list):
        self.head = self.tail = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_after_value(self, data_after, data_to_insert):
        data_index = self.get_index(data_after)
        if data_index < 0:
            print("invalid data after")
            return
        self.insert_at(data_index + 1, data_to_insert)
        
    def remove_at_begining(self):
        if self.head is None:
            print("the list is empty")
            return
        itr = self.head.next
        itr.prev = None
        self.head = itr

    def remove_at_end(self):
        if self.tail is None:
            print("the list is empty")
            return
        itr = self.tail.prev
        itr.next = None
        self.tail = itr

    def remove_at(self, index):
        if self.head is None:
            print("the list is empty")
            return
        if index == 0:
            self.remove_at_begining()
            return
        if index == self.get_length():
            self.remove_at_end()
            return
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                itr.next.prev = itr
                return
            itr = itr.next
            count += 1

    def remove_by_value(self, value):
        val_index = self.get_index(value)
        if val_index < 0:
            print("invalid value")
            return
        self.remove_at(val_index)
        
    def get_length(self):
        if self.head is None:
            return 0

        itr = self.head
        count = 0
        while itr.next:
            itr = itr.next
            count += 1
        return count

    def get_index(self, value):
        if self.head is None:
            return -1

        itr = self.head
        count = 0
        while itr:
            if value == itr.data:
                return count
            count += 1
            itr = itr.next
        return -1

    def print_forward(self):
        if self.head is None:
            print("list is empty")
            return
        itr = self.head
        dlist = ""
        while itr:
            dlist += str(itr.data) + "->"
            itr = itr.next
        print(dlist)

    def print_reverse(self):
        if self.tail is None:
            print("list is empty")
            return
        itr = self.tail
        dlist = ""
        while itr:
            dlist += str(itr.data) + "<-"
            itr = itr.prev
        print(dlist)

if __name__ == "__main__":
    pass
    dllist = doubly_linked_list()
    dllist.insert_at_begining(100)
    dllist.insert_at_begining(200)
    dllist.insert_at_end(300)
    dllist.insert_at_end(400)
    dllist.insert_at_end(500)
    dllist.insert_at_end(500)
    # dllist.insert_values([1,2,3])
    dllist.insert_at(1,300)
    dllist.insert_after_value(300, 500)
    dllist.remove_at_begining()
    dllist.remove_at_end()
    print(dllist.get_length() )
    dllist.remove_at(0)
    # dllist.remove_by_value(500)
    dllist.print_forward()
    dllist.print_reverse()