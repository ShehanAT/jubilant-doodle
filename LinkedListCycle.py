# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        nodes = []
        while(head):
            nodes.append(head)
            head = head.next
            print(nodes)
            if head in nodes:
                return True
        return False 
        
            
        