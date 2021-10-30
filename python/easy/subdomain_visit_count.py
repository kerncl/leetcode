#Question:
'''
A website domain like "discuss.leetcode.com" consists of various subdomains. At the top level, we have "com", at the next level, we have "leetcode.com", and at the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly.
Now, call a "count-paired domain" to be a count (representing the number of visits this domain received), followed by a space, followed by the address. An example of a count-paired domain might be "9001 discuss.leetcode.com".
We are given a list cpdomains of count-paired domains. We would like a list of count-paired domains, (in the same format as the input, and in any order), that explicitly counts the number of visits to each subdomain.
'''

from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_visit = {}
        for domain in cpdomains:
            temp_domain = domain.split(" ")
            subdomain = temp_domain[1].split(".")
            if len(subdomain) > 2:
                temp_subdomain = '{}.{}' .format(subdomain[len(subdomain)-2],subdomain[len(subdomain)-1])
                if temp_subdomain not in domain_visit.keys():   #2 domain
                    domain_visit[temp_subdomain] = temp_domain[0]
                else:
                    domain_visit[temp_subdomain] = int(domain_visit[temp_subdomain]) + int(temp_domain[0])
            if subdomain[len(subdomain)-1] not in domain_visit.keys():  #1 domain
                domain_visit[subdomain[len(subdomain)-1]] = temp_domain[0]
            else:
                domain_visit[subdomain[len(subdomain)-1]] = int(domain_visit[subdomain[len(subdomain)-1]]) + int(temp_domain[0])
            if temp_domain[1] not in domain_visit.keys():   #full domain
                domain_visit[temp_domain[1]] = temp_domain[0]
            else:
                domain_visit[temp_domain[1]] = int(domain_visit[temp_domain[1]]) +int(temp_domain[0])
        #final_domain = []
        #for key, value in domain_visit.items():
        #    final_domain.append(f'{value} {key}')
        return [f'{value} {key}' for key, value in domain_visit.items()]


result = Solution()
domain = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
print('Visisted domain:', result.subdomainVisits(domain))


#Best solution
'''
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counter = {}
        for cp in cpdomains:
            count, dom = cp.split(" ")
            count = int(count)
            dom = dom.split(".")
            subdom = ""
            while dom:
                subdom = dom.pop() + subdom
                if subdom not in counter:
                    counter[subdom] = count
                else:
                    counter[subdom] += count
                subdom = "." + subdom
        return [str(count) + " " + subdom for subdom, count in counter.items()]
'''