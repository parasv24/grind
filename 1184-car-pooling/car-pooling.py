class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        arr = [0] * 1001
        for z,x,y in trips:
            arr[x] += z
            arr[y] -= z

        if arr[0] > capacity:
            return False
        for i in range(1,1001):
            arr[i] += arr[i-1]
            if arr[i] > capacity:
                return False
        return True
        
        