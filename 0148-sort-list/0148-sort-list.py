class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next

        dummy = ListNode(0)
        dummy.next = head
        size = 1

        while size < length:
            prev = dummy
            curr = dummy.next
            while curr:
                left = curr
                right = self.split(left, size)
                curr = self.split(right, size)
                merged = self.merge(left, right)
                prev.next = merged[0]
                prev = merged[1]
            size *= 2
        return dummy.next

    def split(self, head: ListNode, size: int) -> ListNode:
        for _ in range(size - 1):
            if not head:
                break
            head = head.next

        if not head:
            return None

        next_part = head.next
        head.next = None
        return next_part

    def merge(self, left: ListNode, right: ListNode):
        dummy = ListNode(0)
        tail = dummy

        while left and right:
            if left.val <= right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next

        tail.next = left or right

        while tail.next:
            tail = tail.next

        return dummy.next, tail