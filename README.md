# CPE 49 Python Prep

給 2026-10-06 CPE 考前衝刺使用的複習 repository。

目標不是在最後一天重新學完整演算法，而是把最容易轉換成 AC 的能力固定下來：

1. 一顆星題型辨識與快速 implementation
2. Python 3.9 輸入輸出、字串、排序、數學與 simulation
3. 降低 WA：EOF、格式、邊界條件、tie-breaker
4. 先穩定拿 2 題，再攻第 3 題

> CPE 官方目前的評判環境包含 Python 3.9.6；一顆星選集共 49 題。  
> 官方環境與一顆星選集：https://cpe.cse.nsysu.edu.tw/environment.php

## Repo 結構

- [QUICK_REVIEW.md](QUICK_REVIEW.md)：考前高報酬複習順序
- [PYTHON_CHEATSHEET.md](PYTHON_CHEATSHEET.md)：CPE Python 3.9 快速語法
- [EXAM_CHECKLIST.md](EXAM_CHECKLIST.md)：考場與提交前 checklist
- [cpe49/](cpe49/)：官方一顆星 49 題 Python 解答

## 最後一天建議順序

### Tier A：一定要能獨立寫出

- UVA10055 Hashmat the Brave Warrior
- UVA10035 Primary Arithmetic
- UVA100 The 3n + 1 Problem
- UVA10929 You can say 11
- UVA10420 List of Conquests
- UVA10008 What's Cryptanalysis?
- UVA11332 Summing Digits
- UVA10038 Jolly Jumpers
- UVA10812 Beat the Spread!
- UVA11461 Square Numbers
- UVA10071 Back to High School Physics
- UVA10931 Parity
- UVA10193 All You Need Is Love!
- UVA299 Train Swapping
- UVA10189 Minesweeper

### Tier B：看懂後可以快速重寫

- UVA10041 Vito's Family
- UVA10252 Common Permutation
- UVA490 Rotating Sentences
- UVA272 TeX Quotes
- UVA11063 B2-Sequence
- UVA10019 Funny Encryption Method
- UVA10050 Hartals
- UVA10235 Simply Emirp
- UVA10922 2 the 9s
- UVA10057 A mid-summer night's dream
- UVA10062 Tell me the frequencies!
- UVA10226 Hardwood Species
- UVA11150 Cola

### Tier C：最後再碰

其餘需要較多 implementation 細節、特殊格式或較低短期報酬的題目。

## 考場策略

1. 開場先花約 5–10 分鐘掃全部題目，不要預設題號越前越簡單。
2. 優先序：直接公式 → counting/string → simulation → sorting/math → 熟悉的資料結構/演算法。
3. 第一題目標是盡快 AC，先建立穩定分數。
4. 若一題做了約 25–30 分鐘仍沒有明確 implementation 路線，先換題。
5. 不要為了速度亂送 submission；先做最小測資與 edge case。
6. 已有 C++/APCS/CPE Intermediate 背景時，合理策略是先鎖 2 題，再衝第 3 題。

## 49 題索引

| # | UVA | 題目 |
|---:|---:|---|
| 1 | 10041 | Vito's Family |
| 2 | 10055 | Hashmat the Brave Warrior |
| 3 | 10035 | Primary Arithmetic |
| 4 | 100 | The 3n + 1 Problem |
| 5 | 10929 | You can say 11 |
| 6 | 10101 | Bangla Numbers |
| 7 | 10420 | List of Conquests |
| 8 | 10008 | What's Cryptanalysis? |
| 9 | 10222 | Decode the Mad man |
| 10 | 11332 | Summing Digits |
| 11 | 10252 | Common Permutation |
| 12 | 490 | Rotating Sentences |
| 13 | 272 | TeX Quotes |
| 14 | 12019 | Doom's Day Algorithm |
| 15 | 10038 | Jolly Jumpers |
| 16 | 10056 | What is the Probability!! |
| 17 | 10170 | The Hotel with Infinite Rooms |
| 18 | 10268 | 498' |
| 19 | 10783 | Odd Sum |
| 20 | 10812 | Beat the Spread! |
| 21 | 11349 | Symmetric Matrix |
| 22 | 11461 | Square Numbers |
| 23 | 11063 | B2-Sequence |
| 24 | 10071 | Back to High School Physics |
| 25 | 10093 | An Easy Problem! |
| 26 | 948 | Fibonaccimal Base |
| 27 | 10019 | Funny Encryption Method |
| 28 | 10931 | Parity |
| 29 | 11005 | Cheapest Base |
| 30 | 10050 | Hartals |
| 31 | 10193 | All You Need Is Love! |
| 32 | 10190 | Divide, But Not Quite Conquer! |
| 33 | 10235 | Simply Emirp |
| 34 | 10922 | 2 the 9s |
| 35 | 11417 | GCD |
| 36 | 10908 | Largest Square |
| 37 | 10221 | Satellites |
| 38 | 10642 | Can You Solve It? |
| 39 | 10242 | Fourth Point!! |
| 40 | 10057 | A mid-summer night's dream |
| 41 | 10062 | Tell me the frequencies! |
| 42 | 299 | Train Swapping |
| 43 | 10226 | Hardwood Species |
| 44 | 10189 | Minesweeper |
| 45 | 10409 | Die Game |
| 46 | 10415 | Eb Alto Saxophone Player |
| 47 | 118 | Mutant Flatworld Explorers |
| 48 | 11150 | Cola |
| 49 | 11321 | Sort! Sort!! and Sort!!! |

## 使用方式

先不要背答案。每題建議流程：

1. 只看題名，自己說出核心方法。
2. 3–5 分鐘內寫出 skeleton。
3. 再對照本 repo 解答。
4. 特別標記 I/O、termination condition、排序 tie-breaker。
5. 隔一段時間重新空白寫一次。

