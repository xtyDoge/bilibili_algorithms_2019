## 题目
-----

av394281 中，充满威严的蕾米莉亚大小姐因为触犯某条禁忌，被隙间妖怪八云紫（紫m……èi）按住头在键盘上滚动。
同样在弹幕里乱刷梗被紫姐姐做成罪袋的你被指派找到大小姐脸滚键盘打出的一行字中的第 `k` 个仅出现一次的字。
(为简化问题，大小姐没有滚出 ascii 字符集以外的字)

### 输入
每个输入都有若干行，每行的第一个数字为`k`，表示求第`k`个仅出现一次的字。然后间隔一个半角空格，之后直到行尾的所有字符表示大小姐滚出的字符串`S`。

### 输出
输出的每一行对应输入的每一行的答案，如果无解，输出字符串`Myon~`
(请不要输出多余的空行）
为了方便评测，如果答案存在且为c，请输出[c]


## 思路和通过情况
-----
遍历两次字符串，第一次获取仅出现一次的字并存储在hashtable中，第二次找出第k个仅出现一次的字
时间复杂度为`O(n)`，空间复杂度为`O(n)`