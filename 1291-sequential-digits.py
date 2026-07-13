#leetcode 1291 sequential digits
#difficulty:medium
#approach:sliding window
#time complexity:o(1)
#space complexity:o(1)

class Solution(object):
    def sequentialDigits(self, low, high):
        result = []
        digits = "123456789"
        
        min_len = len(str(low))
        max_len = len(str(high))
        
        for length in xrange(min_len, max_len + 1):
            for start in xrange(10 - length):
                num_str = digits[start : start + length]
                num = int(num_str)
                
                if low <= num <= high:
                    result.append(num)
                    
        return result
        