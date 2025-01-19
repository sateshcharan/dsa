class Node:
    def __init__(self, data=None, next=None):
        self.next = next
        self.data = data


class linkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        if self.head == None:
            self.head = Node(data)
            return

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
            if count == index - 1:
                itr.next = Node(data, itr.next)
                return
            count += 1
            itr = itr.next

    def insert_at_end(self, data):
        self.insert_at(self.get_length(), data)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_after_value(self, ref_data, new_data):
        if self.head is None:
            print("list is empty")
            return

        if self.find_index(ref_data) == -1:
            print("data not found")
            return

        self.insert_at(self.find_index(ref_data) + 1, new_data)

    def remove_at_begining(self):
        if self.head is None:
            print("list is empty")
            return

        itr = self.head
        self.head = itr.next

    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            print("invalid index")
            return

        if self.head is None:
            print("the list is empty")
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
        if self.head is None:
            print("list is empty")
            return

        self.remove_at(self.get_length() - 1)

    def remove_by_value(self, value):
        if self.head is None:
            print("list is empty")
            return

        if self.find_index(value) == -1:
            print("data not found")
            return

        self.remove_at(self.find_index(value))

    def get_length(self):

        itr = self.head
        count = 0
        while itr:
            itr = itr.next
            count += 1
        return count

    def find_index(self, data):
        if self.head is None:
            print("the list is empty")
            return

        itr = self.head
        count = 0
        while itr:
            if data == itr.data:
                return count
            itr = itr.next
            count += 1
        return -1

    def print_list(self):
        if self.head == None:
            print("the list is empty")
            return

        itr = self.head
        llist = ""
        while itr:
            llist += str(itr.data) + "-->"
            itr = itr.next
        print(llist)


llist = linkedList()
# llist.insert_at_begining(10)
# llist.insert_at_begining(20)
# llist.insert_at_begining(30)
# llist.insert_at(1, 40)
# llist.insert_at_end(50)
# llist.remove_at_begining()
# llist.remove_at(2)
llist.insert_values([100, 200, 300, 400, 500])
llist.remove_at_end()
llist.remove_at_begining()
llist.remove_at(1)
llist.insert_after_value(200, 300)
llist.remove_at_begining()
llist.print_list()
