from util import ListNode, parseListNode, printListNode
from typing import Optional, List

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        (_, newHead) = self.f(head, n)
        # printListNode(newHead)
        return newHead
        
    def f(self, head, target):
        if head is None:
            return (1, None)
        (n, node) = self.f(head.next, target)

        # print(n, head.val)
        
        if n == target:
            return (n+1, head.next)
        head.next = node
        return (n+1, head)
        
Solution().removeNthFromEnd(parseListNode([1,2,3,4,5]), 2)
