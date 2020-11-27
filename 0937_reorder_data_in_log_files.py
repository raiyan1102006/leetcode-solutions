# 937. Reorder Data in Log Files
# https://leetcode.com/problems/reorder-data-in-log-files/
# Runtime: 36 ms, faster than 63.79% of Python3 online submissions for Reorder Data in Log Files.
# Memory Usage: 14.3 MB, less than 18.22% of Python3 online submissions for Reorder Data in Log Files.

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
    
        def get_key(log):
            _id, rest = log.split(" ", maxsplit=1)
            return (0, rest, _id) if rest[0].isalpha() else (1, )
        # print(sorted([get_key(log) for log in logs]))
        return sorted(logs, key=get_key)