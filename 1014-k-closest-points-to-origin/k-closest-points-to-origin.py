class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res=[]
        for i in range(len(points)):
            ans = (points[i][0]**2 + points[i][1]**2)**0.5
            heapq.heappush(heap, (ans,points[i]))
        heapq.heapify(heap)
        for i in range(k):
            point = heapq.heappop(heap)
            res.append(point[1])
        return res

        