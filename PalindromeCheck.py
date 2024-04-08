

def isPalindrome(string):
    l, r = 0, len(string) - 1
    while l<r:
        if string[l] != string[r]:
            return False
        l, r = l+1, r-1
    return True


phrase = "anitalavalatina"
print(isPalindrome(phrase))
