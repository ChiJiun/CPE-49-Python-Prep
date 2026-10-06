"""UVA 11063 - B2-Sequence
Core: positive strictly increasing terms and all pair sums (i<=j) unique.
Time: O(n^2).
"""

def solve():
    case = 1

    while True:
        try:
            line = input()
        except EOFError:
            break

        if line == "":
            continue

        n = int(line)

        values = []
        while len(values) < n:
            values.extend(list(map(int, input().split())))

        ok = True

        for i in range(n):
            if values[i] <= 0:
                ok = False
            if i > 0 and values[i] <= values[i - 1]:
                ok = False

        seen = set()

        if ok:
            for i in range(n):
                for j in range(i, n):
                    total = values[i] + values[j]

                    if total in seen:
                        ok = False
                        break

                    seen.add(total)

                if not ok:
                    break

        if ok:
            print(f"Case #{case}: It is a B2-Sequence.")
        else:
            print(f"Case #{case}: It is not a B2-Sequence.")

        print()
        case += 1

if __name__ == "__main__":
    solve()
