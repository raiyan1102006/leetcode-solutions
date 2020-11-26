# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer/
# Runtime: 44 ms, faster than 76.11% of Python3 online submissions for Roman to Integer.
# Memory Usage: 14.2 MB, less than 52.03% of Python3 online submissions for Roman to Integer.


class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        i=0
        val_dict = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        while (i<len(s)):
            if i+1<len(s) and val_dict[s[i]]<val_dict[s[i+1]]:
                total += (val_dict[s[i+1]] - val_dict[s[i]])
                i+=2
            else:
                total+=val_dict[s[i]]
                i+=1
        return total
    

