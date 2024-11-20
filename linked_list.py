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
            self.head = Node(data, None)
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
        if index < 0 or index >= self.get_length():
            raise Exception("invalid index")

        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            count += 1
            itr = itr.next

    def insert_after_value(self, data_after, data_to_insert):

        count = 0
        itr = self.head

        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                return
            count += 1
            itr = itr.next

        print("data_after did not match")

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("invalid index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
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

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next
        print(llstr)


if __name__ == "__main__":
    pass
    list = linked_list()
    list.insert_at_begining(1)
    list.insert_at_end(6)
    list.print()
    list.insert_values(["banana", "mango", "grapes", "orange"])
    list.print()
    print(list.get_length())
    list.remove_at(2)
    list.print()
    list.insert_at(1, "Hola")
    list.print()
    list.insert_after_value("Hola", "Vamos")
    list.print()
    list.remove_by_value("Hola")
    list.print()
