## Problem 2

Starting from the root directory(where the program runs) we look for the given folder

print(f"c files: {file_explorer.find_files('.c', 'testdir')}")

for that directory we:

- loop through the listed files:
  for each file: (O(1))
  - if it's a file we check the suffix (string lookup) (O(1))
  - add in list (O(1))
    for each folder: (O(1))
  - if it's a folder we call this function again [recursive](<O(n)>)

Space:
we use - a list for the files we find in a directory (+ subdirectories) - a smaller list for the results (files we were looking for)

Complexity:
worst case would be all the items in the directories to be sub-directories
for n depth we would be going through all of them.

Complexity => O(n)
