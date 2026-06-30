
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        freq = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in  freq:
                freq[sorted_word] = [word]
            else:
                freq[sorted_word].append(word)
        return list(freq.values())
    
strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution().groupAnagrams(strs))
        

