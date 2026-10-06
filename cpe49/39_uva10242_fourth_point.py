"""UVA 10242 - Fourth Point!!
Core: identify the duplicated endpoint; missing parallelogram vertex = a+b-duplicate.
Time: O(1) per case.
"""

def solve():
    while True:
        try:
            values = list(map(float, input().split()))
        except EOFError:
            break

        p1 = (values[0], values[1])
        p2 = (values[2], values[3])
        p3 = (values[4], values[5])
        p4 = (values[6], values[7])

        if p1 == p3:
            duplicate = p1
            a = p2
            b = p4
        elif p1 == p4:
            duplicate = p1
            a = p2
            b = p3
        elif p2 == p3:
            duplicate = p2
            a = p1
            b = p4
        else:
            duplicate = p2
            a = p1
            b = p3

        x = a[0] + b[0] - duplicate[0]
        y = a[1] + b[1] - duplicate[1]

        print(f"{x:.3f} {y:.3f}")

if __name__ == "__main__":
    solve()
