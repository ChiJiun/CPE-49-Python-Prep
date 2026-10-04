"""UVA 10221 - Satellites
Core: convert the angle to radians; compute arc and chord on radius 6440+s.
Time: O(1) per case.
"""
import sys
from math import pi, sin

def solve():
    out = []
    for line in sys.stdin:
        if not line.strip():
            continue
        s_txt, a_txt, unit = line.split()
        radius = 6440.0 + float(s_txt)
        angle = float(a_txt)
        if unit == "min":
            angle /= 60.0
        angle %= 360.0
        if angle > 180.0:
            angle = 360.0 - angle
        theta = angle * pi / 180.0
        arc = radius * theta
        chord = 2.0 * radius * sin(theta / 2.0)
        out.append(f"{arc:.6f} {chord:.6f}")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
