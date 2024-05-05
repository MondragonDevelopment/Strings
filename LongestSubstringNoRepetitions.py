"""
Given a string s, find the length of the longest substring without repeating characters.
"""


def lengthOfLongestSubstring(string):
    lastSeen = {}
    longest = [0,1]
    l = 0
    for r, char in enumerate(string):
        if char in lastSeen:
            l = max(l, lastSeen[char] + 1) # If you have already seen a repeated character and updated l, the next time another character repeats itself, 
                                           # instead of moving forward the left index, it will move backwards as in s = 'abba'. To avoid this you need to 
                                           # use the max function
        if longest[1] - longest[0] < r - l + 1: 
            longest = [l, r+1]  # The longest non-repeating substring doesn't update if it has the same length
        lastSeen[char] = r  # This line updates the position of the last time we saw that particular character
    print(lastSeen, longest)
    return longest[1]-longest[0]


s = "dvdf"
s1 = " "
s2 = "bbbbb"
s3 = "abba"
#print(lengthOfLongestSubstring(s))
#print(lengthOfLongestSubstring(s1))
#print(lengthOfLongestSubstring(s2))
print(lengthOfLongestSubstring(s3))
