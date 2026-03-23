class HashEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]

    # función hash simple
    def _hash(self, key):
        total = 0
        for c in key:
            total += ord(c)
        return total % self.capacity

    def load_factor(self):
        return self.size / self.capacity

    def put(self, key, value):
        index = self._hash(key)
        bucket = self.buckets[index]

        # actualizar si existe
        for entry in bucket:
            if entry.key == key:
                entry.value = value
                return

        bucket.append(HashEntry(key, value))
        self.size += 1

        if self.load_factor() > 0.7:
            self._rehash()

    def get(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]

        for entry in bucket:
            if entry.key == key:
                return entry.value

        return None

    def _rehash(self):
        print("rehash ejecutado...")
        old_buckets = self.buckets

        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0

        for bucket in old_buckets:
            for entry in bucket:
                self.put(entry.key, entry.value)