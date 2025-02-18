# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array, depth = 1):
    # Write your code here.
    total = 0
    for i in range(len(array)):
        if type(array[i]) is list:
            total += (depth+1)*productSum(array[i], depth+1)
        else:
            total += array[i]
    return total 
