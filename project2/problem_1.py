class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.cache = {}
        self.list_of_keys = []
        pass

    def dequeue(self):

        item_to_delete = self.list_of_keys[0]
        # TODO cleanup the list of keys
        del self.cache[item_to_delete]
        self.list_of_keys.remove(item_to_delete)

        print("list of keys {}".format(self.list_of_keys))
        pass

    def enqueue(self, key, value):
        index = self.index(key)
        self.cache[index] = value

        # remove the old key from our key list to keep the new one in the first position
        if(index in self.list_of_keys):
            self.list_of_keys.remove(index)
        self.list_of_keys.append(index)

        print("list of keys {}".format(self.list_of_keys))
        pass

    def get(self, key):
        print("getting : {}".format(key))
        # Retrieve item from provided key. Return -1 if nonexistent.
        index = self.index(key)
        if index in self.cache:
            self.enqueue(key, self.cache[index])
            return self.cache[index]
        return -1

    def index(self, value):
        # Split the hashing of the key to give us more flexibility
        hashval = value
        return hashval

    def set(self, key, value):
        print("setting : {} {}".format(key, value))
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if self.get(key) == -1:
            if len(self.cache) < self.capacity:
                index = self.index(key)
                self.enqueue(key, value)
            else:
                print("memory limit")
                self.dequeue()
                self.set(key, value)
        print("cache {}".format(self.cache))
        pass


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print(
    our_cache.get(1),       # returns 1
    our_cache.get(2),       # returns 2
    our_cache.get(9),      # returns -1 because 9 is not present in the cache

    our_cache.set(5, 5),
    our_cache.set(6, 6),

    # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
    our_cache.get(3),

    our_cache.set(19, 29),
    our_cache.set(38, 28),
    our_cache.set(47, 222),
    our_cache.set(59, 9),
    our_cache.set(82, 8),
    our_cache.get(47),
    our_cache.set(71, 7),
    our_cache.set(95, 9),
    our_cache.set(18, 8),
    our_cache.get(47),
    our_cache.set(99, 9),
    our_cache.set(80, 8),
    our_cache.get(47),
    our_cache.set(39, 9),
    our_cache.set(68, 8),
    our_cache.set(67, 7),
    our_cache.get(69),

)
