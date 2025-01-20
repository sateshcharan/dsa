class HashTable:
    def __init__ (self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    def __setitem__ (self, key, value):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0] == key:
                self.arr[h][idx] = (key, value)
        self.arr[h].append((key,value))

    def __getitem__ (self, key):
        h = self.get_hash(key)
        for idx,element in enumerate(self.arr[h]):
            if element[0] == key:
                return element[1]

    def __delitem__ (self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]

if __name__ == "__main__":
    pass
    htable = HashTable()
    htable["march 6"] = 100
    htable["march 6"] = 78
    htable["march 7"] = 88
    del htable["march 6"]
    print(htable.arr)
    print(htable["march 7"])