# 811. Subdomain Visit Count
# https://leetcode.com/problems/subdomain-visit-count/
# Runtime: 44 ms, faster than 95.97% of Python3 online submissions for Subdomain Visit Count.
# Memory Usage: 14.3 MB, less than 9.98% of Python3 online submissions for Subdomain Visit Count.


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count_dict = defaultdict(lambda:0)
        for element_str in cpdomains:
            number, subdomain = element_str.split(" ")
            splitted_str = subdomain.split(".")
            temp_str = splitted_str.pop()
            count_dict[temp_str] += int(number)
            
            while(len(splitted_str)>0):
                temp_str=splitted_str.pop()+'.'+temp_str
                count_dict[temp_str] += int(number)
        return [str(val)+" "+key for key,val in count_dict.items()]