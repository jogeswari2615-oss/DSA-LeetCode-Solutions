#leetcode 169-majority element
#difficulty:easy
#approach:hash map
#time complexity:O(n)
#space complexity:O(n)
class Solution(object):
    def majorityElement(self, nums):
        count={}
        for num in nums:
            if num in count:
                count[num]+=1
            
            else:
                count[num]=1
            
        for num in count:
            if count[num]>len(nums)//2:
                return num
        
