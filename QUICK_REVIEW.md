# 考前高報酬複習清單

## 1. 最容易直接換成分數的能力

### EOF 與輸入

CPE/UVA 很多一星題真正容易失分的是輸入處理，不是演算法。

熟悉：

- 單行兩整數直到 EOF
- 第一行 testcase 數量
- 0 / 0 0 作為終止條件
- 空白行分隔 testcase
- 整行字串，不能用 split() 破壞空白
- 一題可能跨多行讀資料

### Counting / frequency

最常用：

- dict
- collections.Counter
- set
- sorted(..., key=...)

代表題：

- UVA10420
- UVA10008
- UVA10252
- UVA10062
- UVA10226

### 整數與數學

一定熟：

- abs
- //, %
- gcd
- isqrt
- digit sum
- base conversion
- parity / bit count

代表題：

- UVA10055
- UVA10929
- UVA11332
- UVA10812
- UVA11461
- UVA10193
- UVA10931

### Simulation

先把狀態表示乾淨，再實作規則。

代表題：

- UVA10035
- UVA100
- UVA10050
- UVA10189
- UVA10409
- UVA118

### Sorting

常見陷阱：

- primary / secondary key 方向不同
- tie-breaker
- 負數的 remainder 與 Python % 語意不同

代表題：

- UVA10057
- UVA10062
- UVA299
- UVA11321

---

## 2. 今天的刷題順序

### 第一輪：快速題

1. UVA10055
2. UVA11332
3. UVA10071
4. UVA10931
5. UVA10812
6. UVA10929
7. UVA10420
8. UVA10008

目標：每題看到就知道 1–2 分鐘內怎麼寫。

### 第二輪：典型 simulation / set / sorting

1. UVA10035
2. UVA10038
3. UVA11461
4. UVA10193
5. UVA10050
6. UVA299
7. UVA10189

### 第三輪：補容易 WA 的格式題

1. UVA10252
2. UVA490
3. UVA272
4. UVA10062
5. UVA10226
6. UVA11349

---

## 3. 卡題時的判斷

讀題後先回答四件事：

1. Input 結束條件是什麼？
2. Output 是否有 Case / 空行 / 小數位格式？
3. Constraints 暗示 O(n)、O(n log n) 還是可以 brute force？
4. 這題真正的 state / invariant 是什麼？

若 10 分鐘後連方法都沒有，不要繼續 implementation。

若方法有但 implementation 很長，先掃其他題，確認沒有更便宜的 AC。

---

## 4. AC 前的最小測試

至少自己測：

- 最小值
- 最大或接近上界
- 空集合 / 單元素（若允許）
- 已排序 / 逆序
- 重複值
- 負數（若允許）
- termination condition
- EOF
- tie
