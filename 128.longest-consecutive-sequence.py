#leetcode 128 longest consecutive sequence
#difficulty:medium
#approach:hashmap+greedy
#timecomplexity:o(n)
#spacecomplexity:o(n)
class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        numSet=set(nums)
        longest=0
        for num in numSet:
            if num-1  not in numSet:
                current=num
                length=1
                while current+1 in numSet:
                    current+=1
                    length+=1
                if length>longest:
                   longest=length
        return longest
        