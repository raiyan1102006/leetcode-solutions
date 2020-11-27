# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/
# Runtime: 244 ms, faster than 28.56% of Python3 online submissions for Product of Array Except Self.
# Memory Usage: 21.2 MB, less than 37.91% of Python3 online submissions for Product of Array Except Self.


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        dp_fwd = [nums[0]]+[1 for _ in range(len(nums)-1)]
        dp_bck = [1 for _ in range(len(nums)-1)]+[nums[-1]]

        for i in range(1,len(nums)-1):
            dp_fwd[i] = nums[i]*dp_fwd[i-1]
            
        for i in range(len(nums)-2,0,-1):
            dp_bck[i] = nums[i]*dp_bck[i+1]
        
        output = [dp_bck[1]]
        for i in range(1,len(nums)-1):
            output.append(dp_fwd[i-1]*dp_bck[i+1])
        
        output.append(dp_fwd[-2])
        return(output)