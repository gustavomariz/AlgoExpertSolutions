def twoNumberSum(array, targetSum):
    # Write your code here.
    result = []
    l = len(array)
    
    if l < 2:
        return result
        
    for i in range(l):
            for j in range(i + 1, l):
                if array[j] + array[i] == targetSum:
                    result.append(array[i])
                    result.append(array[j])
                    return result
            
    return result
