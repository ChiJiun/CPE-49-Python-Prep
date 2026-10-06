"""UVA 10055 - Hashmat the Brave Warrior
Core: print the absolute difference for every pair until EOF.
Time: O(1) per case.
"""

def solve():
    while True:
        try:
            a, b = map(int, input().split())
        except EOFError:
            break
        print(abs(a - b))

if __name__ == "__main__":
    solve()
