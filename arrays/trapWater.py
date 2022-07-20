
def computeLeftMax(arr):
    leftMax = [0 for  i in range(len(arr))]

    for i in range(1,len(arr)):
        leftMax[i] = max(leftMax[i-1],arr[i-1])

    return leftMax    

def computeRightMax(arr):
    rightMax = [0 for  i in range(len(arr))]

    for i in range(len(arr)-1-1,-1,-1):
        rightMax[i] = max(rightMax[i+1],arr[i+1])

    return rightMax    


def trapWater(arr):

    leftMax = computeLeftMax(arr)
    rightMax = computeRightMax(arr)

    result = 0 
    for i in range(1,len(arr)-1):
        if(min(rightMax[i],leftMax[i]) > arr[i]):
            result = result + min(rightMax[i],leftMax[i]) - arr[i]

    return result

if __name__ == "__main__":
    print(trapWater([1,0,2,1,3,1,2,0,3]))