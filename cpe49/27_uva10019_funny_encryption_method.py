"""UVA 10019 - Funny Encryption Method
Core: count 1-bits in decimal n and in the value formed by reading decimal digits as hex.
Time: O(number of digits).
"""

def solve():
    t = int(input())

    for _ in range(t):
        n = int(input())

        b1 = bin(n).count("1")
        hex_value = int(str(n), 16)
        b2 = bin(hex_value).count("1")

        print(b1, b2)

if __name__ == "__main__":
    solve()
