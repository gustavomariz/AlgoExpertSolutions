def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()
    if fastest == True:
        blueShirtSpeeds.reverse()

    totalspeed = 0
    for i in range(len(redShirtSpeeds)):
        totalspeed += max(redShirtSpeeds[i], blueShirtSpeeds[i])
    return totalspeed
