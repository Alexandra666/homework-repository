"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    if not a:
        print("Empty lists")
        return 0
    result = 0
    a, b, c, d = sorted(a), sorted(b), sorted(c), sorted(d)
    n = len(a)
    for i in range(n):
        for j in range(n):
            k = 0
            l = n - 1
            while k < n and l >= 0:
                while a[i] + b[j] + c[k] + d[l] > 0 and l >= 0:
                    l -= 1
                if a[i] + b[j] + c[k] + d[l] == 0:
                    result += 1
                    k += 1
                    ll = l - 1
                    while ll >= 0 and d[ll] == d[l]:
                        result += 1
                        ll -= 1
                elif a[i] + b[j] + c[k] + d[l] < 0:
                    k += 1
    return result
