"""UVA 11321 - Sort! Sort!! and Sort!!!
Core: sort by C/C++ remainder, odd before even, odd descending, even ascending.
Time: O(n log n) per case.
"""
import sys

def c_remainder(n, m):
    return n % m if n >= 0 else -((-n) % m)

def sort_key(n, m):
    r = c_remainder(n, m)
    odd = (n % 2 != 0)
    return (r, 0 if odd else 1, -n if odd else n)

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    p = 0
    out = []
    while p + 1 < len(data):
        n, m = data[p], data[p + 1]
        p += 2
        out.append(f"{n} {m}")
        if n == 0 and m == 0:
            break
        a = data[p:p+n]
        p += n
        a.sort(key=lambda x: sort_key(x, m))
        out.extend(map(str, a))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
