# https://leetcode.com/explore/interview/card/amazon/79/sorting-and-searching/2996/
# elapsed : 21 min
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dist = collections.Counter()
        for idx, point in enumerate(points):
            dist[idx] = math.sqrt(point[0]**2 + point[1]**2)
            
        return [points[idx[0]] for idx in dist.most_common()[-1*K:]]
        
