from util import ListNode, parseListNode, printListNode
from typing import Optional, List

def makeCycledList(values, pos):
    ll = parseListNode(values)
    if pos == -1:
        return ll
    lastNode = ll
    while lastNode.next is not None:
        lastNode = lastNode.next
    cl = ll
    while pos > 0:
        cl = cl.next
        pos -= 1
    lastNode.next = cl
    return ll


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            print(None)
            return None
        slow = head.next
        fast = head.next.next

        try:
            while slow != fast:
                slow = slow.next
                fast = fast.next.next
            
            entry = head
            while entry != slow:
                entry = entry.next
                slow = slow.next
            print(entry.val)
            return entry
        except:
            print(None)
            return None
        


Solution().detectCycle(makeCycledList([3,2,0,-4], 1))
Solution().detectCycle(makeCycledList([1,2], 0))
Solution().detectCycle(makeCycledList([1], -1))
Solution().detectCycle(makeCycledList([1, 2, 3], -1))
Solution().detectCycle(makeCycledList([], -1))
Solution().detectCycle(makeCycledList([-1,-7,7,-4,19,6,-9,-5,-2,-5], 9))
