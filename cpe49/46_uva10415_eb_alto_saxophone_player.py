"""UVA 10415 - Eb Alto Saxophone Player
Core: count each finger's transition from released (0) to pressed (1).
Time: O(10 * song length).
"""
import sys

PATTERN = {
    "c":"0111001111", "d":"0111001110", "e":"0111001100",
    "f":"0111001000", "g":"0111000000", "a":"0110000000",
    "b":"0100000000", "C":"0010000000", "D":"1111001110",
    "E":"1111001100", "F":"1111001000", "G":"1111000000",
    "A":"1110000000", "B":"1100000000",
}

def solve():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    t = int(lines[0])
    out = []
    for case in range(t):
        song = lines[case + 1] if case + 1 < len(lines) else ""
        prev = "0000000000"
        presses = [0] * 10
        for note in song:
            cur = PATTERN[note]
            for i in range(10):
                if prev[i] == "0" and cur[i] == "1":
                    presses[i] += 1
            prev = cur
        out.append(" ".join(map(str, presses)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
