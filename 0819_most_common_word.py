# 819. Most Common Word
# https://leetcode.com/problems/most-common-word/
# Runtime: 24 ms, faster than 98.53% of Python3 online submissions for Most Common Word.
# Memory Usage: 14.4 MB, less than 7.24% of Python3 online submissions for Most Common Word.


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        freq = defaultdict(lambda:0)
        paragraph = re.sub(r'[^\w]', ' ', paragraph.lower())

        for word in paragraph.split(" "):
            if word and word not in banned: # valid word
                freq[word]+=1
        k = list(freq.keys())
        v = list(freq.values())
        return k[v.index(max(v))]