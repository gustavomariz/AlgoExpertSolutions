def sortedSquaredArray(array):
    # Write your code here.

    sorted = []

    for i in range(len(array)):
        sorted.append(array[i]*array[i])

    sorted.sort()
    
    return sorted
