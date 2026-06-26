class Solution:
    def trap(self, height: List[int]) -> int:
        trappedWater = []
        for i in range(1,len(height)):
            maxL = max(height[:i])
            maxR = max(height[i:])
            trappedWater.append(max(0,min(maxL,maxR)-height[i]))
        return sum(trappedWater)