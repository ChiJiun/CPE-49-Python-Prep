# Python 3.9 CPE Cheatsheet

## stdin

### 逐行直到 EOF

```python
import sys

for line in sys.stdin:
    line = line.rstrip("\n")
```

### 一次讀完 token

```python
import sys

data = sys.stdin.buffer.read().split()
```

大量純數字通常用這個最穩。

### 保留每一行內容

```python
import sys

lines = sys.stdin.read().splitlines()
```

---

## 常用標準庫

```python
from collections import Counter, defaultdict
from math import gcd, isqrt, sqrt, sin, pi
```

---

## Counter

```python
from collections import Counter

cnt = Counter("banana")
print(cnt["a"])
```

---

## Sorting

```python
a.sort()
a.sort(reverse=True)

items.sort(key=lambda x: (x[0], -x[1]))
```

### ASCII frequency 題

```python
sorted_items = sorted(cnt.items(), key=lambda p: (p[1], -p[0]))
```

---

## Set

```python
seen = set()
seen.add(x)

if x in seen:
    ...
```

---

## 數學

```python
from math import gcd, isqrt

g = gcd(a, b)

r = isqrt(n)
is_square = (r * r == n)
```

---

## 字串

```python
s.isalpha()
s.isdigit()
s.upper()
s.lower()
ord(c)
chr(x)
```

---

## 二進位

```python
b = bin(n)[2:]
ones = b.count("1")
```

---

## Queue

```python
from collections import deque

q = deque([start])
x = q.popleft()
q.append(y)
```

---

## Grid 八方向

```python
DIR8 = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1),
]
```

---

## 小數輸出

```python
print(f"{x:.3f}")
print(f"{x:.4f}")
```

題目要求幾位就印幾位，不要自行決定。

---

## Python 與 C/C++ 負數 remainder 差異

Python：

```python
-5 % 3 == 1
```

C/C++：

```text
-5 % 3 == -2
```

若題目排序規則明確依 C/C++ remainder，可用：

```python
def c_remainder(n, m):
    return n % m if n >= 0 else -((-n) % m)
```

UVA11321 特別要注意。

---

## 一般 solve() 模板

```python
import sys

def solve():
    data = sys.stdin.buffer.read().split()
    # parse / solve / output

if __name__ == "__main__":
    solve()
```

---

## CPE 最重要的 Python 原則

- 不要在考場寫花俏 abstraction。
- 先求正確，再求短。
- 優先標準庫。
- 避免依賴 Python 3.10+ 新語法。
- 大量輸入優先 sys.stdin.buffer。
- Output format 與題目逐字一致。
