class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        rem_arr = [0]*k

        for i in arr:
            rem = i%k
            rem_arr[rem]+=1
        
        if rem_arr[0] % 2 != 0:
            return False
        
        for i in range(1,k//2+1):
            if (rem_arr[i]!=rem_arr[k-i]):
                return False
        
        return True

        