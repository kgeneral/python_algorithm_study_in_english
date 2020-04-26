class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dupPathCount = defaultdict(list)
        for path in paths:
            desc = path.split(" ")
            basepath = desc.pop(0)
            for d in desc:
                p = basepath + "/" + d.split("(")[0]
                dupPathCount[d.split("(")[1]].append(p)
        result = []        
        for v in dupPathCount.values():
            if len(v) > 1:
                result.append(v)
                
        return result
