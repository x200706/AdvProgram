def bubble_sort_and_count_swaps(n, arr):
    swaps = 0
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    return swaps

cases = int(input())
for _ in range(cases):
    length = int(input())
    train = list(map(int, input().split()))
    swaps = bubble_sort_and_count_swaps(length, train)
    print(f"Optimal train swapping takes {swaps} swaps.")