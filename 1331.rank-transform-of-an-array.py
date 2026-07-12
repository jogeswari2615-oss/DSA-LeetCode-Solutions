#leetcode 1331 rank transform of an array
#difficulty:easy
#approach:hashmap and sorting
#time complexity:o(nlogn)
#space complexity:o(n)
class Solution(object):
    def arrayRankTransform(self, arr):
        sorted_unique = sorted(list(set(arr)))
        rank_map = {}
        for rank, num in enumerate(sorted_unique, 1):
            rank_map[num] = rank
            
        return [rank_map[num] for num in arr]