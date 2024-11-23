class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_begining(self, data):
        node = Node(data)
        if self.head == None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def insert_at_end(self, data):
        node = Node(data)
        if self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def insert_values(self, data_list):
        self.head = self.tail = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            print("invalid index")
            return

        if index == 0:
            self.insert_at_begining(data)
            return

        if index == self.get_length():
            self.insert_at_end(data)
            return

        itr = self.head
        count = 0
        node = Node(data)
        while itr:
            if count == index - 1:
                node.next = itr.next
                node.prev = itr
                if itr.next:
                    itr.next.prev = node
                itr.next = node
                break
            count += 1
            itr = itr.next

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            print("the list is empty unable to insert")

        itr = self.head
        node = Node(data_to_insert)
        while itr:
            if itr.data == data_after:
                node.next = itr.next
                node.prev = itr
                if itr.next:
                    itr.next.prev = node
                itr.next = node
                break
            itr = itr.next

        print("unable to find data_after")

    def remove_at_begining(self):
        if self.head is not None:
            self.head = self.head.next
            self.head.prev = None
            return
        else:
            print("linked list is empty")

    def remove_at_end(self):
        itr = self.tail.prev
        itr.next = None
        self.tail = itr

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
                itr.next.prev = itr
                itr.next = itr.next.next
                return
            count += 1
            itr = itr.next

    def remove_by_value(self, data):
        count = 0
        itr = self.head
        while itr:
            if itr.data == data:
                self.remove_at(count)
                break
            count += 1
            itr = itr.next

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def print_forward(self):
        if self.head is None:
            print("linked list is empty")
            return

        itr = self.head
        llist = ""
        while itr:
            llist += str(itr.data) + "-->"
            itr = itr.next
        print(llist)

    def print_backward(self):
        if self.tail is None:
            print("linked list is empty")
            return

        itr = self.tail
        llist = ""
        while itr:
            llist += str(itr.data) + "<--"
            itr = itr.prev
        print(llist)


if __name__ == "__main__":
    pass
    llist = linked_list()
    # llist.insert_at_begining(20)
    # llist.insert_at_end(40)
    # llist.insert_at_end(30)
    llist.insert_values(["banana", "mango", "grapes", "orange"])
    print(llist.get_length())
    llist.insert_at(2, "kiwi")
    # llist.print()
    llist.insert_after_value("kiwi", "strawberry")
    llist.remove_at_begining()
    llist.remove_at_end()
    # llist.remove_at(1)
    # llist.remove_by_value("grapes")
    llist.print_forward()
    llist.print_backward()
    # llist.print()
    # llist.print()
    # llist.print()
    # llist.print()
