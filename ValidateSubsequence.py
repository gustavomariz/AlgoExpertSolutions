def isValidSubsequence(array, sequence):
    k = 0
    for s in sequence:
        while k < len(array) and array[k] != s:
            k += 1
        if k == len(array):  
            return False
        k += 1 
    return True
