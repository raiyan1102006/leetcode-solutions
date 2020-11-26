# 7. Reverse Integer
# https://leetcode.com/problems/reverse-integer/
# Runtime: 28 ms, faster than 83.06% of Python3 online submissions for Reverse Integer.
# Memory Usage: 14.2 MB, less than 40.44% of Python3 online submissions for Reverse Integer.

class Solution:
    def reverse(self, x: int) -> int:
        flag = False
        if x<0:
            flag=True
            x=-x
        
        output = 0
        while(x):
            x,vagshesh = divmod(x,10)
            output = output*10+vagshesh

        if output>(2**31)-1:
            return 0
        return output if not flag else -output
