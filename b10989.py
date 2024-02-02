import sys
A = [int(sys.stdin.readline()) for _ in range(int(input()))]
def quickSort():
    def partition(low, high):
        pivot = A[(low + high) // 2]
        while low <= high:
            while A[low] < pivot: low += 1
            while A[high] > pivot: high -= 1
            if low <= high:
                A[low], A[high] = A[high], A[low]
                low, high = low + 1, high - 1
        return low
    def sort(low, high):
        if low >= high: return
        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)
    sort(0, len(A) - 1)
print("\n".join(map(str, A)))
