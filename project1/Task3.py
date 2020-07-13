"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


def isFixedNumberFromBangalore(number):
    return number[0:5] == "(080)"


def isFixedLine(number):
    return number[0:2] == "(0"


def isTelemarketer(number):
    return number[0:3] == "140"


def isValidMobile(number):
    return number in ["7", "8", "9"]


def getAreaCode(number):
    position = 1
    for char in number[2:]:
        position += 1
        if char == ")":
            break
    return number[1:position]


def getMobileCode(number):
    return number[0:4]


area_codes_called_from_bang = set()
calls_to_and_from_Bangalore = 0
calls_from_fixed_line_in_Bangalore = 0

for call in calls:
    if (isFixedNumberFromBangalore(call[0])):
        calls_from_fixed_line_in_Bangalore += 1
        if (isFixedNumberFromBangalore(call[1])):
            calls_to_and_from_Bangalore += 1
        if isFixedLine(call[1]):
            area_codes_called_from_bang.add(getAreaCode(call[1]))
        elif not (isTelemarketer(call[1])):
            if(isValidMobile(call[1][0])):
                area_codes_called_from_bang.add(getMobileCode(call[1]))
print("The numbers called by people in Bangalore have codes:")
for codeToPrint in (sorted(area_codes_called_from_bang)):
    print(codeToPrint)

print("{:.2f} percent of calls from fixed lines in Bangalore are calls \
to other fixed lines in Bangalore.".format((calls_to_and_from_Bangalore/calls_from_fixed_line_in_Bangalore)*100))
