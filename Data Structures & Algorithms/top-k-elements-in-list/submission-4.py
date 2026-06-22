class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashCount = {}
        for num in nums:
            hashCount[num]= hashCount.get(num,0)+1

        return sorted(hashCount,reverse=True,key=lambda x:hashCount[x])[:k]