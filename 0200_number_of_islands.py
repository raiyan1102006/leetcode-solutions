# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/
# Runtime: 144 ms, faster than 47.99% of Python3 online submissions for Number of Islands.
# Memory Usage: 15.3 MB, less than 32.71% of Python3 online submissions for Number of Islands.


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def my_dfs(row,col):
            if row>=len(grid) or col>=len(grid[0]) or row<0 or col<0 or grid[row][col]=='0':
                return
            
            grid[row][col] = '0'
            my_dfs(row+1,col)
            my_dfs(row-1,col)
            my_dfs(row,col+1)
            my_dfs(row,col-1)
            
     
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]=='1':
                    count+=1
                    my_dfs(row,col)

        return count