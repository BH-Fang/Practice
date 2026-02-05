class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
            dummy = ListNode(next=head)
            lastNode = dummy
            while lastNode.next and lastNode.next.next:
                a = lastNode.next
                b = a.next
                a.next = b.next
                b.next = a
                lastNode.next = b
                lastNode = a
            return dummy.next
    

