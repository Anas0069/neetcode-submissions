class Solution:
    def isValid(self, s: str) -> bool:
            stack = []
            closetoopoen = {'}':'{',')':'(',']':'['}
            for i in s:
                if i in closetoopoen:
                    if stack and stack[-1] == closetoopoen[i]:
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(i)
            return True if not stack else False