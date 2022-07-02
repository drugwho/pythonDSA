"""
Interview Question #2

"A palindrome is a string that reads the same forward and backward"

For example: radar or madam

Our task is to design an optimal algorithm for checking whether a given string is palindrome or not! 

Time: O(N) where n is the number of characters in the word

"""




def palindromeCheckStandalone(word):
    
    isPalindrome = True
    for x in range(0,len(word)):
        if(word[x]!=word[len(word)-x-1]):
            isPalindrome = False

    print(isPalindrome)
    return isPalindrome


"""
This function uses the knowledge from reverseArray
"""
def reverse(word):
    arr = list(word)
    start_index = 0
    end_index = len(arr)-1
    
    while end_index > start_index:
        arr[start_index], arr[end_index] = arr[end_index], arr[start_index]
        start_index+=1
        end_index-=1
    
    # logic to convert ["c","a","t"] to "cat"
    return "".join(arr)

def palindromeCheck(word):

    isPalindrome = True
    if(word!=reverse(word)):
        isPalindrome = False
    print(isPalindrome)    
    return isPalindrome    
    


if __name__ == '__main__':
    palindromeCheck("raghu")
    palindromeCheck("radar")
