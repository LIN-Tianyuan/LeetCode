"""
2. Add Two Numbers
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy node as the start of the result chain table
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        # Iterate through the two linked lists until both reach the end
        while l1 or l2 or carry:
            # Remove the value if there are nodes left in the current chain table, otherwise 0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            # Calculate the sum of the current bits plus rounding
            sum = val1 + val2 + carry
            # Update the feed
            carry = sum // 10
            # Create a new node to hold the value of the current bit
            current.next = ListNode(sum % 10)
            current = current.next

            # Move to the next node
            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy_head.next

