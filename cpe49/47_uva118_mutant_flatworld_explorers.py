"""UVA 118 - Mutant Flatworld Explorers
Core: simulate robots; remember scented edge positions that suppress repeated falls.
Time: O(total instructions).
"""

DIRECTIONS = "NESW"
MOVE = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0),
}

def solve():
    max_x, max_y = map(int, input().split())
    scents = set()

    while True:
        try:
            x, y, direction = input().split()
            instructions = input()
        except EOFError:
            break

        x = int(x)
        y = int(y)
        facing = DIRECTIONS.index(direction)
        lost = False

        for command in instructions:
            if command == "L":
                facing = (facing - 1) % 4

            elif command == "R":
                facing = (facing + 1) % 4

            else:
                current_direction = DIRECTIONS[facing]
                dx, dy = MOVE[current_direction]
                next_x = x + dx
                next_y = y + dy

                if 0 <= next_x <= max_x and 0 <= next_y <= max_y:
                    x = next_x
                    y = next_y

                elif (x, y) in scents:
                    continue

                else:
                    scents.add((x, y))
                    lost = True
                    break

        if lost:
            print(x, y, DIRECTIONS[facing], "LOST")
        else:
            print(x, y, DIRECTIONS[facing])

if __name__ == "__main__":
    solve()
