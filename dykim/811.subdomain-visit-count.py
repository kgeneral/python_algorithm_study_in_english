class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counter = defaultdict(int)
        for cpdomain in cpdomains:
            count = int(cpdomain.split(" ")[0])
            domainParts = cpdomain.split(" ")[1].split(".")
            
            for i in range(len(domainParts)):
                counter[".".join(domainParts[i:])] += count
        
        return [str(counter[key]) + " " + key for key in counter]
