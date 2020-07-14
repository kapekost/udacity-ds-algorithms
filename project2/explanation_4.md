## Problem 4

To solve this problem, we use a Boolean flag within a recursion
The space we consume

- is for that flag
- the array of users, we fetch in the iterations
- the array of groups, we fetch in the iterations

The Time complexity is the recursion depth (n) subdirectories  
 Complexity => O(n)

- Union
  Parsing each array and putting the values in Set, this will give use unique values only
  return a new LinkedList created from the new values.

  Alternatively we can achieve this by using pointers and swapping Nodes

  The space complexity is increased by using a Set()

  Time complexity O(n)+O(m)+O(n+m) n,m items in input lists

  Complexity => O(n)

- intersection
  Create 2 Sets with the elements to take advantage of the Set function of intersection
  similar like before, parsing the 2 arrays and creating a new one.
  The intersection complexity O(m\*n) n,m items in input lists
  Time complexity O(n)+O(m)+O(n^2)+O(z) z, the number of the items after the intersection
  Complexity => O(n^2)
