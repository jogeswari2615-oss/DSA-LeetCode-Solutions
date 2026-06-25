#leetcode 3737-count subarrays with majority element 1
#difficulty:medium
#time complexity:O(n2)
#space complexity:O(1)
class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        n=len(nums)
        ans=0
        for i in range(n):
            count_target=0
            for j in range(i,n):
                if nums[j]==target:
                    count_target+=1
                length=j-i+1
                if count_target>length//2:
                    ans+=1
        return ans