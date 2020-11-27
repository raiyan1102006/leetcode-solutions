# 953. Verifying an Alien Dictionary
# https://leetcode.com/problems/verifying-an-alien-dictionary/
# Runtime: 24 ms, faster than 98.89% of Python3 online submissions for Verifying an Alien Dictionary.
# Memory Usage: 14.4 MB, less than 5.77% of Python3 online submissions for Verifying an Alien Dictionary.


class Solution:
    def ordered(self, word1, word2):
        for chars in zip(*[word1,word2]):
            if self.strDict[chars[0]]>self.strDict[chars[1]]: return False
            if self.strDict[chars[0]]<self.strDict[chars[1]]: return True 

        # by this time, the zip(*) chars are same. So the first str must be smaller
        if word1>word2: return False
        else: return True
        
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        self.strDict = {order[i]:i for i in range(len(order))}
        for word_ind in range(1,len(words)):
            if not self.ordered(words[word_ind-1],words[word_ind]):
                return False
            
        return True
            