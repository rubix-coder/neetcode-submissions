def mul(numbers):
    prod = 1
    for num in numbers:
        prod*=num
    return prod

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_list = []
        print((len(nums)))
        for i in range(len(nums)):
            prod_list.append(mul(nums[:i]+nums[i+1:]))
        return prod_list
        