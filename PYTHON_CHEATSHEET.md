# Python 3.9 CPE Cheatsheet

這個 repo 刻意採用 **`input()` + `map()` + `list()` + `split()` + `print()`** 的考場手寫風格。

EOF 也維持 `input()` 風格，用 `try/except EOFError` 處理。

## 1. 一行固定數量整數

```python
a, b = map(int, input().split())
```

三個：

```python
a, b, c = map(int, input().split())
```

## 2. 一行不固定數量

```python
arr = list(map(int, input().split()))
```

例如：

```text
5 10 20 30 40
```

```python
data = list(map(int, input().split()))
n = data[0]
arr = data[1:]
```

## 3. 第一行是 testcase 數量

```python
t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
```

## 4. 固定讀 N 行

```python
n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))
```

或：

```python
arr = [int(input()) for _ in range(n)]
```

## 5. EOF：不知道有幾組資料

不用 `stdin`，直接：

```python
while True:
    try:
        a, b = map(int, input().split())
    except EOFError:
        break

    print(a + b)
```

這是本 repo 對 EOF 題目的主要寫法。

## 6. EOF：整行字串

```python
while True:
    try:
        s = input()
    except EOFError:
        break

    print(s)
```

`input()` 會移除行尾換行，但會保留行內空格。

## 7. 以 0 結束

```python
while True:
    n = int(input())

    if n == 0:
        break

    print(n)
```

兩個數：

```python
while True:
    a, b = map(int, input().split())

    if a == 0 and b == 0:
        break
```

## 8. map / list

`map()` 是把函式套到每個元素：

```python
a, b = map(int, input().split())
```

若需要真正的 list：

```python
arr = list(map(int, input().split()))
```

### 差別

```python
map(int, input().split())
```

回傳可迭代的 map object。

```python
list(map(int, input().split()))
```

直接得到 list，適合排序、索引、切片。

## 9. 字串

```python
s = input()
words = s.split()
```

注意：

```python
input()
```

保留整行內容；

```python
input().split()
```

會用空白切成多個 token。

## 10. Counter

```python
from collections import Counter

cnt = Counter("banana")
print(cnt["a"])
```

## 11. Sorting

```python
arr.sort()
arr.sort(reverse=True)

items.sort(key=lambda x: (x[0], -x[1]))
```

## 12. Set

```python
seen = set()
seen.add(x)

if x in seen:
    ...
```

## 13. 數學

```python
from math import gcd, isqrt

g = gcd(a, b)

r = isqrt(n)
if r * r == n:
    print("perfect square")
```

## 14. 二進位

```python
b = bin(n)[2:]
ones = b.count("1")
```

## 15. Grid 八方向

```python
DIR8 = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1),
]
```

## 16. 小數輸出

```python
print(f"{x:.3f}")
print(f"{x:.4f}")
```

## 17. Python 與 C/C++ 負數 remainder 差異

Python：

```python
-5 % 3 == 1
```

C/C++：

```text
-5 % 3 == -2
```

UVA11321 可自行寫：

```python
def c_remainder(n, m):
    if n >= 0:
        return n % m
    return -((-n) % m)
```

## 考場建議

優先記這五個：

```python
a, b = map(int, input().split())

arr = list(map(int, input().split()))

t = int(input())

for _ in range(t):
    ...

while True:
    try:
        ...
    except EOFError:
        break
```

原則：**題目怎麼分組，就照題目一行一行讀。**
