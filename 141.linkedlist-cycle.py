#leetcode 141.linked list cycle
#difficulty:easy
#approach:Floyd's Cycle-Finding algorithm
#time complexity:O(N)
#space complexity:O(1)
class Solution(object):
    def hasCycle(self, head):
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False
        