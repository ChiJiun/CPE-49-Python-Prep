"""UVA 10101 - Bangla Numbers
Core: recursively group numbers by kuti, lakh, hajar and shata.
Time: O(number of Bangla groups).
"""

KUTI = 10000000

def bangla(n):
    parts = []

    if n >= KUTI:
        parts.extend(bangla(n // KUTI))
        parts.append("kuti")
        n %= KUTI

    if n >= 100000:
        parts.append(str(n // 100000))
        parts.append("lakh")
        n %= 100000

    if n >= 1000:
        parts.append(str(n // 1000))
        parts.append("hajar")
        n %= 1000

    if n >= 100:
        parts.append(str(n // 100))
        parts.append("shata")
        n %= 100

    if n > 0:
        parts.append(str(n))

    return parts

def solve():
    case = 1

    while True:
        try:
            n = int(input())
        except EOFError:
            break

        parts = bangla(n)

        if len(parts) == 0:
            parts = ["0"]

        print(f"{case:4d}. " + " ".join(parts))
        case += 1

if __name__ == "__main__":
    solve()
