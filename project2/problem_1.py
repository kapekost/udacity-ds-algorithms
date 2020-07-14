class LRU_Cache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.list_of_keys = []
        pass

    def dequeue(self):
        """
        Remove from the cache the item that is first in the list_of_keys
        Then remove that from the list_of_keys too
        """
        item_to_delete = self.list_of_keys[0]
        del self.cache[item_to_delete]
        self.list_of_keys.remove(item_to_delete)
        pass

    def enqueue(self, key, value):
        """
        Add in the cache the key value pare,
        Add the key at the end of the list_of_keys queue 

        Args:
        key: the key of the object to store (hash)
        value: the value to cache
        """
        index = self.index(key)
        self.cache[index] = value

        # if we already had that key in the priority list, we remove it from the old position
        # to have it first
        if(index in self.list_of_keys):
            self.list_of_keys.remove(index)
        self.list_of_keys.append(index)
        pass

    def get(self, key):
        """
        Get the value of the given key from the cache if it exists

        Args:
        key: the key of the object to find (hash)

        Returns:
        the value of the key
        -1 of the value is not found
        """
        # Retrieve item from provided key. Return -1 if nonexistent.
        index = self.index(key)
        if index in self.cache:
            self.enqueue(key, self.cache[index])
            return self.cache[index]
        return -1

    def index(self, value):
        """
        Create a hash for indexing the cache
        (Not implemented)

        Args:
        value: the value we want to use for index

        Returns:
        the same value is returned
        """
        # Split the hashing of the key to give us more flexibility on how we want to calculate the keys
        hashval = value
        return hashval

    def set(self, key, value):
        """
        Set the value if the key is not present in the cache.
        If the cache is at capacity remove the oldest item.
        If the value already exists don't process anthing further

        Args:
        key: the key of the object to store (hash)
        value: the value to cache
        """
        if(key is None or value is None):
            return
        if self.get(key) == -1:
            if len(self.cache) < self.capacity:
                index = self.index(key)
                self.enqueue(key, value)
            else:
                self.dequeue()
                self.set(key, value)

        pass


if __name__ == "__main__":
    print("testing for capacity 5")
    capacity = 5
    our_cache = LRU_Cache(capacity)

    print("set 1 2 3 4")
    for i in range(1, 5):
        our_cache.set(i, i)

    print("get 1, 2, 9")
    assert [our_cache.get(1),  our_cache.get(2),  our_cache.get(9)] == [
        1, 2, -1], f"in cache {our_cache.cache}"
    print('result: 1, 2, -1')

    print("set 5 6, to hit capacity")
    our_cache.set(5, 5),
    our_cache.set(6, 6),

    print("get 3, to be -1")
    # 3 should now be wiped, we added 2 more elements and this was the last one in priority
    assert our_cache.get(3) == -1, f"in cache {our_cache.cache}"

    print("it should ignore setting None values")
    our_cache.set(None, None)

    assert our_cache.cache == {1: 1, 2: 2, 4: 4,
                               5: 5, 6: 6}, f"in cache {our_cache.cache}"
    assert our_cache.get(None) == -1, f"None return -1"

    print("insert many values and track one of them to be in the array before reaching the capacity")
    our_cache.set(100, 100)
    assert our_cache.get(100) == 100, f"get the number to track"

    for i in range(capacity-1):
        our_cache.set(i, i)

    assert our_cache.get(
        100) == 100, f"in cache {our_cache.cache}"

    print("access and validate all the other numbers")
    for i in range(capacity-1):
        assert our_cache.get(i) == i, f"number found {i}"

    print("our last number should still be here, and this access should reset the position back to being first")
    assert our_cache.get(
        100) == 100, f"in cache {our_cache.cache}"

    print("access and validate all the other numbers again, and insert one extra")
    for i in range(capacity-1):
        assert our_cache.get(i) == i, f"number found {i}"

    our_cache.set(200, 200)

    print("now the number we track should be missing")
    assert our_cache.get(
        100) == -1, f"in cache {our_cache.cache}"

    print("adding 1888 numbers and check the last 5 to exist")
    for i in range(1888):
        our_cache.set(i, i)

    for i in range(1888-5, 1888):
        assert our_cache.get(i) == i, f"in cache {our_cache.cache}"

    print("adding 1888001 numbers")
    for i in range(1888001):
        our_cache.set(i, i)

    for i in range(1888001-5, 1888001):
        assert our_cache.get(i) == i, f"in cache {our_cache.cache}"

    print("testing for capacity 10000")
    capacity = 10000
    our_cache = LRU_Cache(capacity)

    print("add negative values")
    for i in range(-100, 200):
        our_cache.set(i, i)
        assert our_cache.get(i) == i, f"in cache {our_cache.cache}"
    for i in range(10000):
        our_cache.set(i, i)
        assert our_cache.get(i) == i, f"in cache {our_cache.cache}"

    print("add one more and check the last missing")
    our_cache.set(10000, 10000)

    assert our_cache.get(0) == -1, f"in cache {our_cache.cache}"
    assert our_cache.get(1) == 1, f"in cache {our_cache.cache}"

    print("expect error in empty input")
    exception = False
    try:
        our_cache.get()
    except TypeError as ex:
        exception = True
    assert exception, f"exception {exception}"

    exception2 = False
    try:
        our_cache.set()
    except TypeError as ex:
        exception2 = True
    assert exception2, f"exception {exception2}"
    print("done")
