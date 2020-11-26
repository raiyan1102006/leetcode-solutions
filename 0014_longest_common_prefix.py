# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/
# Runtime: 24 ms, faster than 97.52% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 14.3 MB, less than 12.63% of Python3 online submissions for Longest Common Prefix.


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output=""
        for tp in zip(*strs):
            if len(set(tp))==1:
                output+=tp[0]
            else:
                return output
        return output