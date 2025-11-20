import re
import sys

#!/usr/bin/env python3
# /c:/Users/pooda/OneDrive/Desktop/AIAC/LAB TEST 3/TASK1.py

def merge(left, right):
    i, j = 0, 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    if i < len(left):
        merged.extend(left[i:])
    if j < len(right):
        merged.extend(right[j:])
    return merged

def merge_sort(arr):
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    merged = merge(left, right)
    # Print the merge step showing how subarrays are combined
    print(f"Merging {left} and {right} -> {merged}")
    return merged

def parse_input(s):
    tokens = re.split(r'[\s,]+', s.strip())
    return [int(t) for t in tokens if t != ""]

if __name__ == "__main__":
    try:
        s = input("Enter integers separated by spaces or commas: ")
        arr = parse_input(s)
    except Exception:
        print("Invalid input. Provide integers separated by spaces or commas.")
        sys.exit(1)

    print("Original:", arr)
    sorted_arr = merge_sort(arr)
    print("Sorted:", sorted_arr)