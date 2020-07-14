## Problem 1

First step was to add a dictionary for the items to cache

- the items should never be duplicated, and the access to the dictionary is efficient
- enqueue and dequeue function to manage the state of the queue
  this allows us to change the type/logic of caching, just by simply adjusting the queue/dequeue functions

- we want to keep the most recently accessed element in the cache,
  for this reason I thought to start aligning the order within the queue swapping items
  but that would increase the Complexity. Accessing an item should remove that item from the queue and
  put it back first. The access will be random. Therefore this solution would be very complex

I found good idea to keep an array of keys separate to hold the order (access priority swap).
since the queue is a dictionary (Set) it doesn't hold duplicates already. The list of keys
can be a simple array that has index(order)
so in case of a get() the only addition in the logic would be to remove an existing key from this new list_f_keys,
and push to the first place the same new value. Instead of managing swaps

```
if(index in self.list_of_keys):
    self.list_of_keys.remove(index)
self.list_of_keys.append(index)
```

Space

- for the dictionary, which can get as many as the capacity, and the key:values that it holds.
  in our current samples it holds values as integers.
- for the array of the keys, again same size as the capacity and integers for single values

Complexity

- dequeue:
  O(n) for both removing the key form the array and the object from the Cache Set
  Complexity => O(n)

- enqueue
  we add a value in the Set (O(1))
  if we find a key in the list of keys, we remove it (O(n))
  and then (+)
  we append the index in the list of keys (O(n))
  Complexity => O(n)

- get
  we do a lookup O(n) and if we hit a result we do an enqueue (O(n)) for that one value
  Complexity => O(n)

- index
  just reassigns and returns the value
  Complexity => O(1)

- set
  performs a get(), O(n)
  in case of a miss we do either an enqueue() (O(n)) or dequeue() (O(n)) followed by a set() (O(n))
  Complexity => O(n)
