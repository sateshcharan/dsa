class Node:
    def __init__(self, data=None, next=None, prev=None):
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

    def insert_values(self, data_list):
        self.head = self.tail = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_at(self, index, data):
        dllength = self.get_length()
        if index < 0 and index >= dllength:
            print("invalid index")
        elif index == 0:
            self.insert_at_begining(data)
        elif index == dllength - 1:
            self.insert_at_end(data)
        else:
            node = Node(data)
            itr = self.head
            count = 0
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
            print("doubly linked list is empty")
        else:
            itr = self.head
            count = 0
            while itr:
                if itr.data == data_after:
                    self.insert_at(count + 1, data_to_insert)
                    break
                count += 1
                itr = itr.next

    def remove_at_begining(self):
        if self.head is None:
            print("doubly linked list is empty")
        else:
            itr = self.head.next
            itr.prev = None
            self.head = itr

    def remove_at_end(self):
        if self.tail is None:
            print("doubly linked list is empty")
        else:
            itr = self.tail.prev
            itr.next = None
            self.tail = itr

    def remove_at(self, index):
        dllength = self.get_length()
        if index < 0 or index >= dllength:
            print("invalid index")
        elif index == 0:
            self.remove_at_begining()
            return
        elif index == dllength - 1:
            self.remove_at_end()
            return
        else:
            itr = self.head
            count = 0
            while itr:
                if count == index - 1:
                    itr.next = itr.next.next
                    itr.next.prev = itr
                    break
                count += 1
                itr = itr.next

    def remove_by_value(self, data):
        if self.head is None:
            print("doubly linked list is empty")
        else:
            itr = self.head
            count = 0
            while itr:
                if itr.data == data:
                    self.remove_at(count - 1)
                    break
                count += 1
                itr = itr.next

    def get_length(self):
        if self.head is None:
            print("doubly linked list is empty")
        else:
            itr = self.head
            count = 0
            while itr:
                count += 1
                itr = itr.next
            return count

    def print_forward(self):
        if self.head is None:
            print("doubly linked list is empty")

        else:
            itr = self.head
            dllist = ""
            while itr:
                dllist += str(itr.data) + "-->"
                itr = itr.next
            print(dllist)

    def print_backward(self):
        if self.tail is None:
            print("doubly linked list is empty")

        else:
            itr = self.tail
            dllist = ""
            while itr:
                dllist += str(itr.data) + "<--"
                itr = itr.prev
            print(dllist)


if __name__ == "__main__":
    pass
    dllist = doubly_linked_list()
    # dllist.insert_at_begining(20)
    # dllist.insert_at_begining(40)
    # dllist.insert_at_end(20)
    # dllist.insert_at_end(40)
    dllist.insert_values(["banana", "mango", "grapes", "orange"])
    print(dllist.get_length())
    dllist.insert_at(2, "kiwi")
    dllist.insert_after_value("kiwi", "strawberry")
    dllist.remove_at_begining()
    dllist.remove_at_end()
    dllist.remove_at(1)
    dllist.remove_by_value("grapes")
    dllist.print_forward()
    dllist.print_backward()
