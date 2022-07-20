"""
The problem is that we want to sort a T[] one-dimensional array of integers
in O(N) running time - and without any extra memory.
The array can contain values: 0, 1 and 2.

Three Way Partition 
O(N)
"""


def dnf(arr, mid):

# i represents the array item to be swapped with currentItem if currentItem is less than pivot(mid = 1)
# end represents the array item to be swapped with currentItem if currentItem is greater than pivot(mid = 1)
    
    currentItem = 0 
    i = 0
    end = len(arr)-1

    while currentItem <= end:
        if(arr[currentItem]<mid):
            arr[i] ,arr [currentItem] = arr[currentItem], arr[i]
            i+=1
            currentItem+=1 
        elif (arr[currentItem]>mid):
            arr[currentItem] ,arr [end] = arr[end], arr[currentItem]
            end -=1
        else:
            currentItem += 1        

    return arr


print(dnf([2,0,1,0,2,0,1,0,1],1))