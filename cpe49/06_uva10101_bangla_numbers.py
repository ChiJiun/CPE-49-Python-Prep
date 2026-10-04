"""UVA 10101 - Bangla Numbers
Core: recursively group numbers by kuti (10^7), then lakh/hajar/shata.
Time: O(number of Bangla groups).
"""
import sys

KUTI = 10_000_000

def bangla(n):
    parts = []
    if n >= KUTI:
        parts.extend(bangla(n // KUTI))
        parts.append("kuti")
        n %= KUTI
    if n >= 100_000:
        parts.extend([str(n // 100_000), "lakh"])
        n %= 100_000
    if n >= 1_000:
        parts.extend([str(n // 1_000), "hajar"])
        n %= 1_000
    if n >= 100:
        parts.extend([str(n // 100), "shata"])
        n %= 100
    if n:
        parts.append(str(n))
    return parts

def solve():
    out = []
    case = 1
    for token in sys.stdin.buffer.read().split():
        n = int(token)
        parts = bangla(n) or ["0"]
        out.append(f"{case:4d}. " + " ".join(parts))
        case += 1
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
