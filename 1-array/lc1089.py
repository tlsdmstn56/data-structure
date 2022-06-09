class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        L = len(arr)
        skip_next = 0
        for i in range(L):
            if arr[i] > 0 or skip_next:
                skip_next = False
                continue
            for j in range(L-1, i, -1):
                arr[j] = arr[j-1]
            arr[i] = 0
            skip_next = True
