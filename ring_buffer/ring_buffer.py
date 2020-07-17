class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.overwrites = 0

    def append(self, item):
        if self.overwrites == self.capacity:
            self.overwrites = 0
        if len(self.storage) == self.capacity:
            self.storage[self.overwrites] = item
            self.overwrites += 1
        else:
            self.storage.append(item)

    def get(self):
        return self.storage