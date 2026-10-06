"""UVA 948 - Fibonaccimal Base
Core: greedily represent n with Fibonacci weights 1,2,3,5,...
Time: O(log n) per case.
"""

def fib_repr(n):
    if n == 0:
        return "0"

    fib = [1, 2]

    while fib[-1] <= n:
        fib.append(fib[-1] + fib[-2])

    if fib[-1] > n:
        fib.pop()

    result = ""
    remain = n

    for value in reversed(fib):
        if value <= remain:
            result += "1"
            remain -= value
        else:
            result += "0"

    return result

def solve():
    t = int(input())

    for _ in range(t):
        n = int(input())
        print(f"{n} = {fib_repr(n)} (fib)")

if __name__ == "__main__":
    solve()
