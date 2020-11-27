# 1197. Minimum Knight Moves
# https://leetcode.com/problems/minimum-knight-moves/


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if (x,y)==(0,0): return 0
        visited= set((0,0))

        queue = collections.deque([(0,0,0)]) # (x,y,level)
        while(queue):
            current_x, current_y, current_lev = queue.popleft()
            for mv_x,mv_y in [(2,1),(2,-1),(1,2),(-1,2),(-2,1),(-2,-1),(1,-2),(-1,-2)]:
                new_x,new_y = current_x+mv_x, current_y+mv_y
                if (new_x,new_y) == (x,y):
                    return current_lev+1
                if (new_x,new_y) not in visited:
                    visited.add((new_x,new_y))
                    queue.append((new_x,new_y,current_lev+1))