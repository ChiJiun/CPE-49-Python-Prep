"""UVA 10268 - 498'
Core: evaluate the derivative of a polynomial at x using Horner's rule.
Time: O(degree).
"""

def solve():
    while True:
        try:
            x = int(input())
            coefficients = list(map(int, input().split()))
        except EOFError:
            break

        degree = len(coefficients) - 1
        answer = 0

        for i in range(degree):
            answer = answer * x + coefficients[i] * (degree - i)

        print(answer)

if __name__ == "__main__":
    solve()
