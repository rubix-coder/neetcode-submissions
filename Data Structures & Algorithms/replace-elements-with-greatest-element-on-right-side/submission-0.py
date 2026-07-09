class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        newArr = []
        for i in range(len(arr)-1):
            newArr.append(max(arr[i+1:]))
        newArr.append(-1)
        return newArr