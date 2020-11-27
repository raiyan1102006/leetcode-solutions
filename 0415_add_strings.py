# 415. Add Strings
# https://leetcode.com/problems/add-strings/
# Runtime: 36 ms, faster than 82.03% of Python3 online submissions for Add Strings.
# Memory Usage: 14.8 MB, less than 10.53% of Python3 online submissions for Add Strings.


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        output = []
        carry = 0
        num1 = list(num1)
        num2 = list(num2)
        while(num1 or num2 or carry):
            x = ord(num1.pop())-ord('0') if num1 else 0
            y = ord(num2.pop())-ord('0') if num2 else 0
            sum_ = x+y+carry
            carry, vagshesh = divmod(sum_,10)
            output.append(vagshesh)
        return "".join([str(x) for x in output[::-1]])
        