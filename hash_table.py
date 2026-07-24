class HashTable:
    def __init__(self, capacity=16, load_factor_limit=0.75):
        self._capacity = capacity
        self._size = 0
        self._load_factor_limit = load_factor_limit
        self._buckets = [[] for _ in range(capacity)]

    def __len__(self):
        return self._size

    def _hash(self, key):
        return hash(key) % self._capacity

    def put(self, key, value):
        if self._size / self._capacity >= self._load_factor_limit:
            self._resize()

        index = self._hash(key)
        bucket = self._buckets[index]
        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self._size += 1

    def get(self, key, default=None):
        index = self._hash(key)
        bucket = self._buckets[index]
        for existing_key, value in bucket:
            if existing_key == key:
                return value
        return default

    def delete(self, key):
        index = self._hash(key)
        bucket = self._buckets[index]
        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                del bucket[i]
                self._size -= 1
                return True
        return False

    def contains(self, key):
        index = self._hash(key)
        return any(existing_key == key for existing_key, _ in self._buckets[index])

    def _resize(self):
        old_buckets = self._buckets
        self._capacity *= 2
        self._buckets = [[] for _ in range(self._capacity)]
        self._size = 0
        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)

    def load_factor(self):
        return self._size / self._capacity

    def longest_chain(self):
        return max((len(b) for b in self._buckets), default=0)
