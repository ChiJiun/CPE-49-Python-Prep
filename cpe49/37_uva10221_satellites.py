"""UVA 10221 - Satellites
Core: convert the angle to radians; compute arc and chord on radius 6440+s.
Time: O(1) per case.
"""
from math import pi, sin

def solve():
    while True:
        try:
            s, angle, unit = input().split()
        except EOFError:
            break

        radius = 6440.0 + float(s)
        angle = float(angle)

        if unit == "min":
            angle /= 60.0

        angle %= 360.0

        if angle > 180.0:
            angle = 360.0 - angle

        theta = angle * pi / 180.0
        arc = radius * theta
        chord = 2.0 * radius * sin(theta / 2.0)

        print(f"{arc:.6f} {chord:.6f}")

if __name__ == "__main__":
    solve()
