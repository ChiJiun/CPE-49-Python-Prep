# 考前高報酬複習清單

本 repo 採用考場手寫優先風格：**`input()`、`map()`、`list()`、`split()`、`print()`**。
EOF 題使用 `try/except EOFError`。

## 1. 最容易直接換成分數的能力

### 輸入先判斷資料怎麼分組

常見四種：

```python
# 一行兩個整數
a, b = map(int, input().split())

# 一行多個整數
arr = list(map(int, input().split()))

# 第一行 T
t = int(input())
for _ in range(t):
    ...

# EOF
while True:
    try:
        ...
    except EOFError:
        break
```

注意：

- 空格分隔 → `.split()`
- 整行字串 → 直接 `input()`
- 第一行 testcase 數量 → 用 `for _ in range(t)`
- `0` / `0 0` 結束 → 讀到 sentinel 後 `break`
- EOF → `try/except EOFError`
- 空白行可能是 testcase 的一部分時，不要隨便跳過

### Counting / frequency

最常用：

- `dict`
- `collections.Counter`
- `set`
- `sorted(..., key=...)`

代表題：UVA10420、UVA10008、UVA10252、UVA10062、UVA10226。

### 整數與數學

一定熟：

- `abs`
- `//`, `%`
- `gcd`
- `isqrt`
- digit sum
- base conversion
- parity / bit count

### Simulation

先把狀態表示乾淨，再照規則更新。

代表題：UVA10035、UVA100、UVA10050、UVA10189、UVA10409、UVA118。

### Sorting

常見陷阱：

- primary / secondary key 方向不同
- tie-breaker
- 負數 remainder 與 Python `%` 語意不同

## 2. 今天的刷題順序

第一輪：UVA10055、11332、10071、10931、10812、10929、10420、10008。

第二輪：UVA10035、10038、11461、10193、10050、299、10189。

第三輪：UVA10252、490、272、10062、10226、11349。

## 3. 卡題時先回答

1. Input 是 T、sentinel 還是 EOF？
2. 一行是一組資料，還是可能跨行？
3. Output 是否有 Case / 空行 / 小數位格式？
4. Constraints 暗示什麼複雜度？
5. state / invariant 是什麼？

若約 25–30 分鐘仍沒有明確 implementation 路線，先換題。
