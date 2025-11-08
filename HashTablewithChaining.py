# Hash Table with Chaining

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.num_elements = 0

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))
        self.num_elements += 1
        self._resize_if_needed()

    def search(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self.hash_function(key)
        initial_len = len(self.table[index])
        self.table[index] = [(k, v) for k, v in self.table[index] if k != key]
        if len(self.table[index]) < initial_len:
            self.num_elements -= 1

    def _resize_if_needed(self):
        load_factor = self.num_elements / self.size
        if load_factor > 0.7:
            old_table = self.table
            self.size *= 2
            self.table = [[] for _ in range(self.size)]
            self.num_elements = 0
            for chain in old_table:
                for key, value in chain:
                    self.insert(key, value)

    def display(self):
        print("Hash Table Contents:")
        for i, chain in enumerate(self.table):
            print(f"Bucket {i}: {chain}")

# Test with new example names

if __name__ == "__main__":
    ht = HashTable()

    # Insert integer keys
    int_keys = [11, 34, 7, 11, 29, 3]
    for i, key in enumerate(int_keys):
        ht.insert(key, i)
    print("\nAfter inserting integer keys:")
    ht.display()

    # Insert string keys
    str_keys = ["pear", "mango", "cherry", "pear", "plum"]
    for i, key in enumerate(str_keys):
        ht.insert(key, i)
    print("\nAfter inserting string keys:")
    ht.display()

    # Insert mixed keys (strings and numbers)
    mixed_keys = [202, "kiwi", 58, "peach", 202]
    for i, key in enumerate(mixed_keys):
        ht.insert(key, i)
    print("\nAfter inserting mixed keys:")
    ht.display()

    # Search examples
    print("\nSearch Examples:")
    print("Search 34:", ht.search(34))
    print("Search 'cherry':", ht.search("cherry"))
    print("Search 999 (non-existent):", ht.search(999))

    # Delete examples
    print("\nDelete Examples:")
    ht.delete(11)
    ht.delete("pear")
    ht.delete(999)  # non-existent key
    ht.display()
