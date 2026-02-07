class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        last_sorted_node = dummy
        while list1 and list2:
            if list2.val < list1.val:
                last_sorted_node.next = list2
                list2 = list2.next
            else:
                last_sorted_node.next = list1
                list1 = list1.next
            last_sorted_node = last_sorted_node.next
        last_sorted_node.next = list1 if list1 else list2
        return dummy.next