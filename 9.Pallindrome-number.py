#leetcode 9.pallindrome number
#difficulty:easy
#approach:string manipultion pattern
#timecomplexity:o(n)
#space complexity:o(n)
class Solution(object):
    def isPalindrome(self, x):
        s=str(x)
        return s==s[::-1]