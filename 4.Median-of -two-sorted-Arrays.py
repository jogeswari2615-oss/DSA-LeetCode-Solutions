#leetcode 4.median of two sorted arrays
#difficulty:Hard
#approach:Merge+sorting
#timecomplexity:o(m+n)log(m+n)
#spacecomplexity:o(m+n)
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        merged=nums1+nums2
        merged.sort()
        n=len(merged)
        if n%2==1:
            return float (merged[n//2])
        else:
            middle1=merged[n//2-1]
            middle2=merged[n//2]
            return(middle1+middle2)/2.0
        