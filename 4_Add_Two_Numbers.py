# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # Takes the list, converts it into
        # a string and returns the reversed 
        # string
        def return_num(l1: ListNode):
            num = ''
            
            while(l1 != None):
                num = num + str(l1.val)
                l1 = l1.next
            return num[::-1]
        
        # create the list for the sum
        def create_list(s):
            length = len(s)
            r1 = ListNode(s[length - 1])
            
            l = len(s) - 2
            temp = r1
            
            while (l >= 0):
                r2 = ListNode(s[l])      
                temp.next = r2          
                temp = temp.next
                l -= 1         
            return r1
        
        n1 = return_num(l1)
        n2 = return_num(l2)
        
        s = str(int(n1) + int(n2))
        
        print(s)
        
        res = create_list(s)
        
        return res
