class hash_table:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None


if __name__ == "__main__":
    pass
    htable = hash_table()
    htable["world"] = 100
    htable["world1"] = 130
    print(htable.arr)
    del htable["world"]
    print(htable.arr)
    print(htable["world1"])
