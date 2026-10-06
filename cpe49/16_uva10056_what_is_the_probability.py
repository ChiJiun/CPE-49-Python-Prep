"""UVA 10056
Core: evaluate a finite repeating geometric process.
Time: O(1) per case.
"""

def solve():
    t = int(input())

    for _ in range(t):
        n, p, i = input().split()
        n = int(n)
        p = float(p)
        i = int(i)

        if p == 0.0:
            answer = 0.0
        else:
            q = 1.0 - p
            answer = p * q ** (i - 1) / (1.0 - q ** n)

        print(f"{answer:.4f}")

if __name__ == "__main__":
    solve()
