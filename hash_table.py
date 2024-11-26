class hash_table:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def add_item(self, key):
        h = self.get_hash(key)
        self.arr[h] = key


if __name__ == "__main__":
    pass
    htable = hash_table()
    htable.add_item("hello")
    htable.add_item("world")
    print(htable.arr)
