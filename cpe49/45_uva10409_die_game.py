"""UVA 10409 - Die Game
Core: simulate the six face values while rolling in four directions.
Time: O(number of commands).
"""

def solve():
    while True:
        n = int(input())

        if n == 0:
            break

        top = 1
        north = 2
        east = 4
        south = 5
        west = 3
        bottom = 6

        for _ in range(n):
            command = input()

            if command == "north":
                top, north, south, bottom = south, top, bottom, north
            elif command == "south":
                top, north, south, bottom = north, bottom, top, south
            elif command == "east":
                top, east, west, bottom = west, top, bottom, east
            elif command == "west":
                top, east, west, bottom = east, bottom, top, west

        print(top)

if __name__ == "__main__":
    solve()
