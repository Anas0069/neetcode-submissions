class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        target = 0
        for i,n in enumerate(nums):
            if i > 0  and nums[i] == nums[i-1]:
                continue
            l,r = i+1 , len(nums) - 1 
            while l<r:
                threesum = n + nums[l] + nums[r]
                if threesum > target:
                    r -= 1
                elif threesum < target:
                    l += 1
                else:
                    res.append([n,nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
        return res
                


      