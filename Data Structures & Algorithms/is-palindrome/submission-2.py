class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs=""
        for i in range(len(s)):
            if not s[i].isalnum():
                continue
            strs += s[i].lower()
        return strs==strs[::-1]
        