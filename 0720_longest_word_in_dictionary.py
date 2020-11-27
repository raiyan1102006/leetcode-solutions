# 720. Longest Word in Dictionary
# https://leetcode.com/problems/longest-word-in-dictionary/
# Runtime: 84 ms, faster than 63.73% of Python3 online submissions for Longest Word in Dictionary.
# Memory Usage: 14.7 MB, less than 43.75% of Python3 online submissions for Longest Word in Dictionary.


class Solution:
    def longestWord(self, words: List[str]) -> str:
#         def len_char(word):
#             return (-len(word),word)
#         sorted_list = sorted(words, key=len_char)
        sorted_list = sorted([(-len(word),word) for word in words])
        for _,word in sorted_list:
            if all([word[:k] in words for k in range(1,len(word))]):
                return word
        
        
            
            
            
