class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n==0:
            return nums1
        for i in range(n):
            nums1.append(nums2[i])
        nums1.sort()
        for i in range(n):
            nums1.remove(0)
      
        