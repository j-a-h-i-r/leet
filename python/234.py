from util import ListNode, parseListNode
from typing import Optional

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None
        h = head
        while h:
            val = h.val
            node = ListNode(val, rev)
            rev = node
            h = h.next
        
        while rev and head:
            if rev.val != head.val:
                return False
            rev = rev.next
            head = head.next
        return True
        
Solution().isPalindrome(parseListNode([1,2,2,1]))
Solution().isPalindrome(parseListNode([1,2]))
Solution().isPalindrome(parseListNode([1,1,2,1]))