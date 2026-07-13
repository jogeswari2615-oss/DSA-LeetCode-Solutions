#leetcode 49 group anagrams
#difficulty:medium
#approach:hashmap
#timecomplexity:o(nxklogk)
#spacecomplexity:o(nxk)
class Solution(object):
    def groupAnagrams(self, strs):
        groups={}
        for word in strs:
            key="".join(sorted(word))
            if key not in groups:
                groups[key]=[]
            groups[key].append(word)
        return groups.values()
        