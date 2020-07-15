## Problem 3

# Huffman Encoding

The process is split in functions based on the steps we need to take to encode and decode a string
Space complexity:

- we use Nodes that hold 2 child nodes, a value and a character.
  The number of nodes depends on the unique characters of the string we are Encoding
  For the steps in the process, we use:
  step 1
- an array of frequencies,
- a dictionary for the count of the frequency of the letters
- an array for the nodes we want to start merging
  while we merge, we use a new node, and we eliminate 2 other each time

For the huffman_code we use a dictionary for the table we want to return,
and an array for the current path calculation

for the encoding we use a string that we append the characters

Time complexity:

- get frequency nodes: - loop though the characters in the string (O(n)) - create an array of tuples with the count of each letter (O(1)) - sort the tuples based on frequency O(n log n) - loop through the tuples and create Nodes for all of them (O(m)) m is the amount of unique letters (tuples)
  return the array of nodes
  O(n log(n))

- pass the nodes to merge_min_nodes until we are left with one root nodes
  for m unique letters of the string we will run this process m times (O(m))
  (because in each step we need to sort again) O(n log(n)) - in every recursion we pick the first 2 nodes and create a new tree - loop through the remaining nodes to add them in the new tree to return
  O(m) + O(n(log(n)))

- Using the tree we just created, we can navigate to the leafs, which hold the letters
  The path to the leaf is the one we need to use to represent the letter that lives in the leaf
  Since the tree is balanced binary tree, the process will have complexity:
  O(log(n))

- Last step is to loop through the letters we want to encode and replace them with the binary representation
  that we got from the previous step, respectively
  O(n) n is the size of the string we want to encode

O(n log(n)) + O(m) + O(n(log(n))) + O(log(n)) + O(n) for all the letters are different m == n

Complexity => O(n\*log(n))

# Decoding Huffman

input is the encoded string, and the tree of nodes with leafs to be the letter we want to find

for space we don't use anything extra

Time Complexity:

for each bit (n) in the string, we navigate in the tree.

Complexity => O(n)
