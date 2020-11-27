# 797. All Paths From Source to Target
# https://leetcode.com/problems/all-paths-from-source-to-target/


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def allPathsToTarget(el):
            if el==len(graph)-1:
                return [[el]]
            
            output_ = []
            for el2 in graph[el]:
                pathlist = allPathsToTarget(el2)
                if pathlist:
                    for path in pathlist:
                        output_.append([el]+path)
                
            return output_ if len(output_) else None
        return(allPathsToTarget(0))