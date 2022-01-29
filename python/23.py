from typing import List, Optional
from util import ListNode, parseListNode, printListNode
import heapq
import itertools

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        counter = itertools.count()
        for l in lists:
            if l:
                h.append((l.val, next(counter), l))
        
        heapq.heapify(h)

        dummy = ListNode()
        dummyCopy = dummy

        while h:
            mn = heapq.heappop(h)
            _, _, node = mn

            if node.next:
                heapq.heappush(h, (node.next.val, next(counter), node.next))

            dummy.next = node
            dummy = dummy.next
            node.next = None

        # print(printListNode(dummyCopy.next))
        return dummyCopy.next

Solution().mergeKLists([parseListNode(l) for l in [[1,4,5],[1,3,4],[2,6]] ])
Solution().mergeKLists([parseListNode(l) for l in [] ])