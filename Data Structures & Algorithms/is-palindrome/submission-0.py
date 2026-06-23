class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = [char.lower() for char in s if char.isalnum()]
        return cleaned_text==cleaned_text[::-1]