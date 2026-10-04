"""UVA 948 - Fibonaccimal Base
Core: greedily represent n with Fibonacci weights 1,2,3,5,...
Time: O(log n) per case.
"""
import sys

def fib_repr(n):
    if n == 0:
        return "0"
    fib = [1, 2]
    while fib[-1] <= n:
        fib.append(fib[-1] + fib[-2])
    if fib[-1] > n:
        fib.pop()
    bits = []
    remain = n
    for f in reversed(fib):
        if f <= remain:
            bits.append("1")
            remain -= f
        else:
            bits.append("0")
    return "".join(bits)

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    out = []
    for n in data[1:1+t]:
        out.append(f"{n} = {fib_repr(n)} (fib)")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
