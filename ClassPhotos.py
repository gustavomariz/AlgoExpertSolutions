def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    redShirtHeights.sort()
    blueShirtHeights.sort()
    
    tag = None
    diff = (redShirtHeights[0] - blueShirtHeights[0])
    if diff < 0:
        tag = "blue"
    if diff > 0:
        tag = "red"
    if diff == 0:
        return False
    for i in range(1, len(redShirtHeights)):
        diff = (redShirtHeights[i] - blueShirtHeights[i])
        if tag == "blue":
            if diff >= 0:
                return False
        if tag == "red":
            if diff <= 0:
                return False
          
    return True
