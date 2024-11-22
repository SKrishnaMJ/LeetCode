class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        dict1=dict(Counter(nums1))
        dict2=dict(Counter(nums2))
        if len(nums1)>len(nums2):
            for k,v in dict1.items():
                if k in dict2.keys():
                    value = min(v,dict2[k])
                    res+=[k]*value
        else:
            for k,v in dict2.items():
                if k in dict1.keys():
                    value = min(v,dict1[k])
                    res+=[k]*value
        return res
        