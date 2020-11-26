# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/
# Runtime: 28 ms, faster than 79.57% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 14.3 MB, less than 19.21% of Python3 online submissions for Valid Parentheses.


class Solution:
    def isValid(self, s: str) -> bool:
        open_ = {'(':1,'{':2,'[':3}
        close_ = {')':1,'}':2,']':3}
        if s[0] in close_:
            return False
        my_stack = []
        for char in s:
            if char in open_:
                my_stack.append(open_[char])
            if char in close_:
                if not len(my_stack): return False
                if my_stack.pop()!=close_[char]:
                    return False
        
        return True if not len(my_stack) else False