"""UVA 10415 - Eb Alto Saxophone Player
Core: count each finger's transition from released (0) to pressed (1).
Time: O(10 * song length).
"""

PATTERN = {
    "c": "0111001111",
    "d": "0111001110",
    "e": "0111001100",
    "f": "0111001000",
    "g": "0111000000",
    "a": "0110000000",
    "b": "0100000000",
    "C": "0010000000",
    "D": "1111001110",
    "E": "1111001100",
    "F": "1111001000",
    "G": "1111000000",
    "A": "1110000000",
    "B": "1100000000",
}

def solve():
    t = int(input())

    for _ in range(t):
        song = input()
        previous = "0000000000"
        presses = [0] * 10

        for note in song:
            current = PATTERN[note]

            for i in range(10):
                if previous[i] == "0" and current[i] == "1":
                    presses[i] += 1

            previous = current

        print(*presses)

if __name__ == "__main__":
    solve()
