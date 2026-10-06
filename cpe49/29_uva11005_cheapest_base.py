"""UVA 11005 - Cheapest Base
Core: compute representation cost in each base 2..36 and keep every minimum.
Time: O(35 * log n) per query.
"""

def read_n_ints(n):
    values = []

    while len(values) < n:
        values.extend(list(map(int, input().split())))

    return values

def representation_cost(n, base, cost):
    if n == 0:
        return cost[0]

    total = 0

    while n > 0:
        digit = n % base
        total += cost[digit]
        n //= base

    return total

def solve():
    t = int(input())

    for case in range(1, t + 1):
        cost = read_n_ints(36)
        q = int(input())

        if case > 1:
            print()

        print(f"Case {case}:")

        for _ in range(q):
            n = int(input())
            costs = []

            for base in range(2, 37):
                current = representation_cost(n, base, cost)
                costs.append((current, base))

            best = min(item[0] for item in costs)
            answer = []

            for current, base in costs:
                if current == best:
                    answer.append(str(base))

            print(f"Cheapest base(s) for number {n}: " + " ".join(answer))

if __name__ == "__main__":
    solve()
