class Solution:
    def mul(self,numbers):
        prod = 1
        for num in numbers:
            prod*=num
        return prod

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_list = []
        for i in range(len(nums)):
            prod_list.append(self.mul(nums[:i]+nums[i+1:]))
        return prod_list
        