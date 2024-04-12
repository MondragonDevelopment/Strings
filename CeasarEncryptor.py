def ceasarEncrypt(string, key):
    newString = ""
    for letter in string:
        nLC = ord(letter) + key
        if nLC <= ord('z'):
            newString += (chr(nLC))
        else: 
            newString += chr(nLC%122 + 96) # If key < 26, also: nLC - 26
    return newString


print(ceasarEncrypt("xyz", 2))
