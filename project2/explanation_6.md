## Problem 6

Space complexity and logic:

basic linked list:
The Node hold a value and the next node
The linked list length determines the space

appending and size calculations use 1-2 vars for node and counter

- Union:
  Thought to use the Set as it will have performance of O(1) and we won't have to perform a lookup for existing values
  Then structuring a new linked list to return seems faster than re-arranging nodes that are connected between each other, parsing one node will need our algorithm to pass through all the ones between (and move pointers)

it will have the size of the unique elements picked from both arrays
worst case will be all of them being unique. sizeA + SizeB

- Intersection:
  for the intersection we use 2 sets, one for each input
  Using set here allows us to do the intersection with the & operator and then structure a new linked list to return
  and one more for the result of the intersection,
  we can optimize space but would make things less readable

Time:

- Union:
  looping through list one to add in our set (O(n)+1) (n elements of 1st list)
  looping through list2 and add in set (O(m)+1) (m elements of 2nd list)
  loop through the generated set to create and append nodes (O(k)+(O(l))) k the elements in the set, and l the size of the list where the new Node will attach at the end
  Complexity => O(n)

- intersection:
  looping through list one to add in set1 (O(n)+1) (n elements of 1st list)
  looping through list2 and add in set2 (O(m)+1) (m elements of 2nd list)
  perform Python & (O(n)) # https://wiki.python.org/moin/TimeComplexity%20%28SetCode%29
  loop through the generated set to create and append nodes (O(k)+(O(l))) k the elements in the set, and l the size of the list where the new Node will attach at the end
  Complexity => O(n)
