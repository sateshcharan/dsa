class HashTable:
    def __init__ (self):
        self.MAX = 10
        self.arr = [ None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def get_probe_range(self, index):
        return [*range(index, len(self.arr))] + [*range(0, index)]

    def find_slot(self, key):
        h = self.get_hash(key)
        probe_range = self.get_probe_range(h)
        for probe in probe_range:
            if self.arr[probe] is None:
                return probe
            if self.arr[probe][0] == key:
                return probe
        raise Exception('htable full')

    def __setitem__ (self, key, value):
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = (key, value)
        else:
            self.arr[self.find_slot(key)] = (key, value)

    def __getitem__ (self, key):
        h = self.get_hash(key)
        if self.arr[h][0] == key:
            return self.arr[h][1]
        else:
            return self.arr[self.find_slot(key)][1]
    
    def __delitem__ (self, key):
        h = self.get_hash(key)
        if self.arr[h][0] == key:
            del self.arr[h]
        else:
            del self.arr[self.find_slot(key)]

if __name__ == "__main__":
    pass
    t = HashTable()
    t['march'] = 3
    t['march'] = 4
    t["march 17"] = 29
    t["april 3"]=234234
    t['may'] = 5
    print(t['march'])
    del t['may']
    del t['may']
    print(t.arr)