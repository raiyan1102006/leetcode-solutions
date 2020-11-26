# 127. Word Ladder
# https://leetcode.com/problems/word-ladder/
# Runtime: 116 ms, faster than 79.37% of Python3 online submissions for Word Ladder.
# Memory Usage: 17.9 MB, less than 17.77% of Python3 online submissions for Word Ladder.

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        hashDict = defaultdict(lambda:[])
        L = len(beginWord)
        for word in wordList:
            for i in range(L):
                hashDict[word[:i]+"*"+word[i+1:]].append(word)
        
        visited=set()
        queue=collections.deque([(beginWord,1)])
        while(queue):
            current_word,level = queue.popleft()
            for i in range(L):
                new_word = current_word[:i]+'*'+current_word[i+1:]
                for ww in hashDict[new_word]:
                    # if ww in visited: continue
                    if ww==endWord:
                        return level+1
                    if ww not in visited:
                        visited.add(ww)
                        queue.append((ww,level+1))
                hashDict[new_word] = []
        return 0