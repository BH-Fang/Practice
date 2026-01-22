
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        a = ListNode(0)
        total = 0
        carry = 0
        ans_current = a

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1 + v2 + carry
            carry = total // 10
            val = total % 10
            ans_current.next = ListNode(val)
            ans_current = ans_current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return a.next