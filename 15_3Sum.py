# 15. 3Sum
# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(nums2, target):
            h={}
  
            for i in range(len(nums2)):
                compl = target - nums2[i]
                if compl not in h:
                    h[nums2[i]] = i
                else: 
                    if (nums2[i],compl,-target) not in self.output_:
                        self.output_.add((nums2[i],compl,-target))

        self.output_ = set()
        nums = sorted(nums)

        for i in range(len(nums)-2):
            twoSum(nums[i+1:],-nums[i])