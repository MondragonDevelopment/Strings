"""
You are given two strings, one which is regularly longer. Write a program that finds every instance of the substring inside the longer one, 
even if its next to itself or overlaps; and then underscorify it. You should return the underscorified string.
"""

def underscorifySubstring(string, substring):
    locations = collapse(getLocations(string, substring))
    return underscorify(string, locations)


def getLocations(string, substring):
    locations = []
    startIdx = 0
    while startIdx < (len(string) - len(substring) + 1):
        nextIdx = string.find(substring, startIdx)
        if nextIdx != -1:
            locations.append([nextIdx, nextIdx + len(substring)])
            startIdx = nextIdx + 1
        else:
            break
    return locations


def collapse(locations):
    if not len(locations):
        return locations
    collapsed = [locations[0]]
    for i in range(1, len(locations)):
        if locations[i][0] <= collapsed[-1][1]:
            collapsed[-1][1] = locations[i][1]
            # newloc = [collapsed[-1][0], locations[i][1]]
            # collapsed.pop()                                   These lines are not necessary. It's way better if done the other way (rewriting it)
            # collapsed.append(newloc)
        else:
            collapsed.append(locations[i])
    return collapsed


def underscorify(string, locations):
    locationsIdx, stringIdx = 0, 0 # Because we are traversing them at the same time
    inbetweenUnderscores = False
    finalChars = []
    i = 0                                                               # This is a dynamic index, tells you if you are at the start or end of the collapsed locations array
    while stringIdx < len(string) and  locationsIdx < len(locations):
        if stringIdx == locations[locationsIdx][i]:                     # This checks if we found the substring in this strIdx posotion
            finalChars.append("_")
            inbetweenUnderscores = not inbetweenUnderscores             
            if not inbetweenUnderscores:                                # If you have finished appending the collapsed substring into finalChars, then you move to the next location
                locationsIdx += 1
            i = 0 if i == 1 else 1
        finalChars.append(string[stringIdx])
        stringIdx += 1
    if locationsIdx < len(locations):                                   # If you reached the end of the string but not locations, then it's because an underscore is needed
        finalChars.append("_")
    elif stringIdx < len(string):                                       # If you traversed every location but not the string, just slice it to the end and append that
        finalChars.append(string[stringIdx:])
    return "".join(finalChars)


string = "testthis is a testtest to see if testestest it works"
substring = "test"
print(underscorifySubstring(string, substring))
