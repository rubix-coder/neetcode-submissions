class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashCount = {}
        cnt = 0
        for num in nums:
            hashCount[num]=hashCount.get(num,0)+1
        list_num = sorted(hashCount.keys(), key=lambda x: hashCount[x])
        return list_num[-k:]