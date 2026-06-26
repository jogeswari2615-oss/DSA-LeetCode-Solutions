#leetcode 3739 Count subarrays with majority element2
#difficulty:hard
#approach:prefix sum,fenwick tree
#timecomplexity:O(nlogn)
#spacecomplexity:O(n)
class Solution(object):
    def countMajoritySubarrays(self, nums, target):

        class BinaryIndexedTree(object):
            def __init__(self, n):
                self.n = n
                self.bit = [0] * (n + 1)

            def update(self, i, val):
                while i <= self.n:
                    self.bit[i] += val
                    i += i & -i

            def query(self, i):
                s = 0
                while i > 0:
                    s += self.bit[i]
                    i -= i & -i
                return s

        n = len(nums)
        tree = BinaryIndexedTree(2 * n + 1)

        prefix = n + 1
        tree.update(prefix, 1)

        ans = 0

        for x in nums:
            if x == target:
                prefix += 1
            else:
                prefix -= 1

            ans += tree.query(prefix - 1)
            tree.update(prefix, 1)

        return ans
        
        