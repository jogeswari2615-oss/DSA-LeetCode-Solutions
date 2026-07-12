#leetcode 217-contains duplicate
#difficulty:easy
#approach:hashmap
#timecomplexity:O(n)
#spacecomplexity:O(n)
class Solution(object):
    def containsDuplicate(self, nums):
       count={}
       for num in nums:
        if num in count:
            return True
        else:
            count[num]=1
       return False