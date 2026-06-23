class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = [char.lower() for char in s if char.isalnum()]
        return cleaned_text==cleaned_text[::-1]


# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = s.lower()
        
#         leftP = 0
#         rightP = len(s) - 1

#         while leftP < rightP:
#             while leftP < rightP and not s[leftP].isalnum():
#                 leftP += 1
#             while leftP < rightP and not s[rightP].isalnum():
#                 rightP -= 1

#             if s[leftP] != s[rightP]:
#                 return False
            
#             leftP += 1
#             rightP -= 1
#         return True