"""UVA 10041 - Vito's Family
Core: the median minimizes the sum of absolute distances.
Time: O(n log n) per case.
"""

def solve():
    t = int(input())
    for _ in range(t):
        data = list(map(int, input().split()))
        n = data[0]
        a = data[1:1+n]
        a.sort()
        m = a[n // 2]
        print(sum(abs(x - m) for x in a))

if __name__ == "__main__":
    solve()
