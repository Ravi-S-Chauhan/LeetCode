# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1,head)
        fast = slow = dummy
        count = 0
        while n != count:
            fast = fast.next
            count += 1
        while fast.next is not None:
            slow,fast = slow.next,fast.next
        slow.next = slow.next.next
        return dummy.next
        