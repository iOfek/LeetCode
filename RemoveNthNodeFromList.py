# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head, n):
        start = ListNode(0)
        start.next = head
        left = start
        right = start
        for i in range(n+1):
            right = right.next
        
        while right is not None:
            right = right.next
            left = left.next    
            
        left.next = left.next.next
        return start.next
def main():
    head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
    n = 2
    object = Solution()
    print(object.removeNthFromEnd(head,n))


if __name__ == "__main__":
    main()