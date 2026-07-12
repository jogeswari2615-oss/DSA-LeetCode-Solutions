#leetcode 219-contains duplicate 2
#difficulty:easy
#approach:hashmap
#timecomplexity:o(n)
#spacecomplexity:o(n)
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        hashmap={}
        for i in range(len(nums)):
            num=nums[i]
            if num in hashmap:
                if i-hashmap[num]<=k:
                    return True
            hashmap[num]=i
        return False
