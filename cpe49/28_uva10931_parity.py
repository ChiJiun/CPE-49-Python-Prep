"""UVA 10931 - Parity
Core: convert an integer to binary and count set bits.
Time: O(log n).
"""

def solve():
    while True:
        n = int(input())

        if n == 0:
            break

        binary = bin(n)[2:]
        ones = binary.count("1")

        print(f"The parity of {binary} is {ones} (mod 2).")

if __name__ == "__main__":
    solve()
