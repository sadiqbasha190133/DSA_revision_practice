class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)

        if s_len != t_len:
            return False
        
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        for char in t:
            freq[char] = freq.get(char, 0) - 1
            if freq[char] < 0:
                return False
        return True

s = "anagram"
t = "nagaram"

print(Solution().isAnagram(s, t))