"""
def longestPalindrome(string):
    longest = float("-inf")
    
    for i in range(len(string)):
        r = len(string) - 1
        while i<r:
            if longest > (len(string) - i):
                break
            if string[i] != string[r]:
                r -= 1
            else:
                if not isPalindrome(string[i:r+1]):
                    r -= 1
                    continue
                else:
                    longest = max(r-i+1, longest)
                    print(string[i:r+1])
                    break
    return longest


def isPalindrome(string):
    l, r = 0, len(string) - 1
    while l < r:
        if string[l] != string[r]:
            return False
        l, r = l+1, r-1
    return True
"""

"""
# O(n^2) time | O(1) space

def longestPalindrome(string):
    currentLongest  = [0, 1]
    for i in range(1, len(string)):
        odd = getLongestPalindromeFrom(string, i - 1, i + 1)
        even = getLongestPalindromeFrom(string, i - 1, i)
        longest = max(odd, even, key = lambda x: x[1] - x[0]) # This lambda function gets the length of the substring based on the way it's stored (duple)
        currentLongest = max(longest, currentLongest, key = lambda x: x[1] - x[0])
    return string[currentLongest[0]:currentLongest[1]]


def getLongestPalindromeFrom(string, leftIdx, rightIdx):
    while leftIdx >= 0 and rightIdx < len(string):
        if string[leftIdx] != string[rightIdx]:
            break
        leftIdx, rightIdx = leftIdx - 1, rightIdx + 1
    return [leftIdx + 1, rightIdx]
"""

def longestPalindrome(s):
    res = ""
    resLen = 0

    for i in range(len(s)):
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r-l+1) > resLen:
                res = s[l:r+1]
                resLen = r - l + 1
            l, r = l - 1, r + 1
        
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r-l+1) > resLen:
                res = s[l:r+1]
                resLen = r - l + 1
            l, r = l - 1, r + 1
    return res

    
print(longestPalindrome('abaxyzzyxjh'))
print(longestPalindrome('babad'))
print(longestPalindrome('cbbd'))