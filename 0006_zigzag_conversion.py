# 6. ZigZag Conversion
# https://leetcode.com/problems/zigzag-conversion/


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1: return s
        output_table = [["" for _ in range(len(s))] for _ in range(numRows)]
        queue = collections.deque(list(s))
        current_index = [0,0]
        upward= False
        
        while(queue):
            current_ = queue.popleft()
            output_table[current_index[0]][current_index[1]] = current_
            if upward: # go diagonally, stop at top
                if current_index[0]==0:
                    current_index[0] += 1
                    upward = False
                else:
                    current_index[1]+=1
                    current_index[0]-=1
                
            else: #go down, stop at bottom
                if current_index[0]==numRows-1:
                    current_index[0]-=1
                    current_index[1]+=1
                    upward = True
                else:
                    current_index[0]+=1

        output = ""
        for row in output_table:
            output+= "".join(row) 

        return(output)