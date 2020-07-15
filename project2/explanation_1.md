## Problem 1

First step was to add a Ordered dictionary for the items to cache

- enqueue and dequeue function to manage the state of the queue
  only "trick" needed here was to add remove an item when we access it,
  both operations are O(1), seems better than managing the order separately

```
 self.cache[index] = self.cache.pop(index)
        return self.cache[index]
```

Space

- for the dictionary, which can get as many as the capacity, and the key:values that it holds.
  in our current samples it holds values as integers.

Complexity

- get
  we do a couple of checks if the key exists and the capacity is not 0
  then we return the key from the set after doing a little pop / insert (all 3 actions O(1))
  Complexity => O(1)

- index
  just reassigns and returns the value
  Complexity => O(1)

- set
  a few of checks for input (O(1))
  a check for capacity and pop() (all O(1))
  return the value from the set() (O(1))
  Complexity => O(1)
