"""
Construct an algorithm to check whether two words (or phrases) are anagrams or not!

"An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once"

For example: restful and fluster

O(NLOGN)
"""

def anagramCheck(inpA,inpB):
    result = False
    if(len(inpA)!= len(inpB)):
        return result

    stA = sorted(list(inpA))
    stB = sorted(list(inpB))

    if(stA == stB):
        return True

    return result



print(anagramCheck("restful","fluster"))    