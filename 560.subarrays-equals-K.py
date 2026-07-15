#leetcode 560 subarray sum equals k
#difficulty:medium
#approach:prefix sum+hashmap
#time complexity:o(n)
#space complexity:o(n)
class Solution(object):
    def subarraySum(self, nums, k):
        prefix=0
        count=0
        hashmap={0:1}
        for num in nums:
            prefix+=num
            if prefix-k in hashmap:
                count+=hashmap[prefix-k]
            if prefix not in hashmap:
                hashmap[prefix]=1
            else:
                hashmap[prefix]+=1
        return count