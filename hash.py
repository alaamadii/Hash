class Hash:
    def __init__(self,capacity=8):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity
        self.DELETED = object()
    def _hash(self, key):
        return hash(key) % self.capacity
    def _probe(self, key):
        index = self._hash(key)
        i = 0
        while True:
            new_index = (index + i * i) % self.capacity
            slot = self.table[new_index]
            if slot is None or slot == self.DELETED or slot[0] == key:
                return new_index
            i += 1
    def _rehash(self):
        old_table = self.table
        self.capacity *= 2
        self.table = [None] * self.capacity
        self.size = 0

        for slot in old_table:
            if slot is not None and slot != self.DELETED:
                self.insert(slot[0], slot[1])

    def insert(self, key, value):
        if (self.size + 1) / self.capacity > 0.7:
            self._rehash()

        index = self._probe(key)
        if self.table[index] is None or self.table[index] == self.DELETED:
            self.size += 1
        self.table[index] = (key, value)

    def search(self, key):
        index = self._hash(key)
        i = 0
        while True:
            new_index = (index + i * i) % self.capacity
            slot = self.table[new_index]

            if slot is None:
                return None  # not found
            if slot != self.DELETED and slot[0] == key:
                return slot[1]
            i += 1
            if i == self.capacity:
                return None  # full cycle, key not found

    def delete(self, key):
        index = self._hash(key)
        i = 0
        while True:
            new_index = (index + i * i) % self.capacity
            slot = self.table[new_index]

            if slot is None:
                return False  # not found
            if slot != self.DELETED and slot[0] == key:
                self.table[new_index] = self.DELETED
                self.size -= 1
                return True
            i += 1
            if i == self.capacity:
                return False
ht = Hash()

ht.insert(1, "A")
ht.insert(2, "B")
ht.insert(3, "C")
print(ht.search(2))
ht.delete(2)
print(ht.search(2))
ht.insert(4, "D")
ht.insert(5, "E")
ht.insert(6, "F")
ht.insert(7, "G")
print(ht.search(7))
