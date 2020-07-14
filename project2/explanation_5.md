## Problem 5

Here We need to create a list that the head will be at the last Node
each node has a link to the previous.

This link is a reference using a hash code that we get when we create a new Block(Node)

Under the main class of Block_chain I decided to create a function to call the Block class that creates a Block with the given data (timestamp, data, and the previous_hash)

I initialize the previous_hash with None so it will be used for the last (firstly created) Block

The function takes as input an array of the data we want to create the chain with

-- created a function to add nodes, which is getting called from the create_chain.

a delete Block would be a loop holding the previous node while we get the one we want to delete.
we change the pointer from the previous in the loop to point to where the one we are deleting is pointing. not sure if it's a requirement

because the indexes are custom (Hashes, we need to return the hash pointing to the head of the chain, and the array (chain itself)) so we can combine the hashes to go through the cain table

The space complexity is increasing based on the Blocks we are adding, containing data + timestamp + 2 hash values

- append block we are not using additional resources, just the block we are creating to add
- create chain, is the main one that creates the array (chain and triggers the add block)

Time complexity:

- append_block:
  we are using the creation of Block which needs the time to
  - create timestamp (I guess O(1) reading the value from some hash)
  - create hash (might be O(n) with n affected by our input data)
    we insert a node in a dictionary (O(1))

complexity => O(n)

- create_chain
  with n as the number of data in our input array
  we call the append block n times
  O (n^2)

  complexity => O(n^2)
