class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        dummy = ListNode(0)
        lastSortedNode = dummy
        
        while True:
            minValue = 10 ** 4 + 1 
            index = -1
            for i, n in enumerate(lists):
                if n and n.val < minValue:
                    minValue = n.val
                    index = i
            if index == -1: break
            lastSortedNode.next =  lists[index]
            lastSortedNode = lastSortedNode.next
            lists[index] = lists[index].next
        return dummy.next