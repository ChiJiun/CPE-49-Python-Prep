"""UVA 11005 - Cheapest Base
Core: compute representation cost in each base 2..36 and keep every minimum.
Time: O(35 * log n) per query.
"""
import sys

def repr_cost(n, base, cost):
    if n == 0:
        return cost[0]
    total = 0
    while n:
        n, digit = divmod(n, base)
        total += cost[digit]
    return total

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    p = 1
    out = []
    for case in range(1, t + 1):
        cost = data[p:p+36]
        p += 36
        q = data[p]
        p += 1
        if case > 1:
            out.append("")
        out.append(f"Case {case}:")
        for _ in range(q):
            n = data[p]
            p += 1
            costs = [(repr_cost(n, base, cost), base) for base in range(2, 37)]
            best = min(c for c, _ in costs)
            bases = [str(base) for c, base in costs if c == best]
            out.append(f"Cheapest base(s) for number {n}: " + " ".join(bases))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
