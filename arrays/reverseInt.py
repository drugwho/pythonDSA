"""
Our task is to design an efficient algorithm to reverse a given integer.
For example if the input of the algorithm is 1234 then the output should be 4321.

for lists : mod ten to pop last number and then divide by ten
"""

def reverseInt(input):
    return int(str(input)[::-1])

print(reverseInt(1004))    