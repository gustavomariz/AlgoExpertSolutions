def binarySearch(array, target):
    # Write your code here.
    return bsassist(array,target,0,len(array)-1)

def bsassist(array, target, left, right):

    if left > right:
        return -1

    mid = (left + right) // 2
    if target == array[mid]:
        return mid
    elif target < array[mid]:
        return bsassist(array,target,left,mid-1)
    else:
        return bsassist(array, target, mid+1, right)
