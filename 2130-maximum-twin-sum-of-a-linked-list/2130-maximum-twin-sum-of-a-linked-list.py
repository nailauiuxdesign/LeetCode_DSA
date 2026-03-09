class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        slow = fast = head

        #find mid
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reverse second half
        prev = None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next

        #calculate max sum
        max_sum = 0
        while prev:
            max_sum = max(max_sum, head.val + prev.val)
            head = head.next
            prev = prev.next

        return max_sum
