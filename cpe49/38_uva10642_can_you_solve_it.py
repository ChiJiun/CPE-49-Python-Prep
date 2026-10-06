"""UVA 10642 - Can You Solve It?
Core: map (x,y) to its index on diagonal traversal, then subtract indices.
Time: O(1) per case.
"""

def position(x, y):
    s = x + y
    return s * (s + 1) // 2 + x

def solve():
    t = int(input())

    for case in range(1, t + 1):
        x1, y1, x2, y2 = map(int, input().split())
        answer = position(x2, y2) - position(x1, y1)
        print(f"Case {case}: {answer}")

if __name__ == "__main__":
    solve()
