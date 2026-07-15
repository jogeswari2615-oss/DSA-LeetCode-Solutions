#leetcode 3658 GCD of odd and even sums
#difficulty:easy
#approach:number theory
#time complexity:o(1)
#space complexity:o(1)
class Solution(object):
    def gcdOfOddEvenSums(self, n):
        # Because GCD(n^2, n*(n+1)) simplifies directly to n
        return n