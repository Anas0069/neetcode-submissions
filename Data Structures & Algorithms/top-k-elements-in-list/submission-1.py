class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        for n in nums:
            count[n] = 1+count.get(n,0)
        for n,c in count.items():
            freq[c].append(n) #n is number value c is index for here in freq we are taking the key as the count frequency and value as number value

        res = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res