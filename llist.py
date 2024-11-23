class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class linked_list:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, self.head)
            self.head = node
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            print("invalid index")
            return

        if index == 0:
            self.insert_at_begining(data)
            return

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
            count += 1
            itr = itr.next

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            print("the list is empty unable to insert")

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                return
            itr = itr.next

        print("unable to find data_after")

    def remove_at_begining(self):
        if self.head is not None:
            self.head = self.head.next
            return
        else:
            print("linked list is empty")

    def remove_at_end(self):
        llist_length = self.get_length() - 2
        itr = self.head
        count = 0
        while itr:
            if count == llist_length:
                itr.next = None
                return
            count += 1
            itr = itr.next

    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            print("invalid index")
            return

        if self.head == None:
            print("linked list is empty")
            return

        if index == 0:
            self.remove_at_begining()
            return

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                return
            count += 1
            itr = itr.next

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def print(self):
        if self.head is None:
            print("linked list is empty")
            return

        itr = self.head
        llist = ""
        while itr:
            llist += str(itr.data) + "-->"
            itr = itr.next
        print(llist)


if __name__ == "__main__":
    pass
    llist = linked_list()
    # llist.insert_at_begining(10)
    # llist.insert_at_end(30)
    llist.insert_values(["banana", "mango", "grapes", "orange"])
    llist.print()
    # print(llist.get_length())
    # llist.insert_at(4, "kiwi")
    # llist.print()
    # llist.insert_after_value("kiwi", "strawberry")
    # llist.print()
    llist.remove_at_begining()
    llist.print()
    llist.remove_at_end()
    llist.print()
    llist.remove_at(1)
    llist.print()
