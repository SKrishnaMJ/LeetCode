class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        setx=set()
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                setx.add(nums1[i])
        return list(setx)
                
        