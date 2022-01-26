from typing import Optional
from util import ListNode, parseListNode, printListNode

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        numNodes = 0
        tail = None

        cur = head
        tail = None
        while cur:
            numNodes += 1
            tail = cur
            cur = cur.next
        
        k = k % numNodes
        # print("K", k)
        skip = numNodes - k - 1
        
        cur = head
        while skip > 0:
            skip -= 1
            cur = cur.next
        
        # print("Taile", tail.val)
        # print("Cur", cur.val)
        
        tail.next = head
        newHead = cur.next
        cur.next = None
        # printListNode(newHead)
        return newHead

Solution().rotateRight(parseListNode([1,2,3,4,5]), 2)
Solution().rotateRight(parseListNode([0, 1, 2]), 4)