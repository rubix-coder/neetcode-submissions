class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        frequency = defaultdict(int)
        # O(n)
        for num in nums:
            frequency[num] += 1
        
        # O(n)
        buckets = defaultdict(list)
        for key, value in frequency.items():
            buckets[value].append(key)
        
        # O(n)
        result = []
        num = 0
        for i in range(n, 0, -1):
            if i in buckets:
                num += len(buckets[i])
                for key in buckets[i]:
                    result.append(key)
            if num >= k:
                break
        return result