class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) % 2 == 1:
            return False
        
        pairs = { '(': ')' , '{': '}' , '[': ']'}
        
        stack = []
        for elem in s:
            if elem in pairs.keys():
                stack.append(elem)
            else:
                if (len(stack) != 0):
                    top = stack[len(stack) - 1]
                else:
                    top = 0
                stack.append(elem)
                if (pairs.get(top) == elem):
                    stack.pop()
                    stack.pop()
              
        if len(stack) == 0:
            return True
        
        return False
