class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = list(zip(position, speed))
        stack = []
        for p,s in sorted(pair)[::-1]: #p is the position and s in the speed
            time = (target - p)/s        
            stack.append(time)
            if len(stack) >= 2 and stack[-2]>= stack[-1]:
                stack.pop()
        return len(stack)