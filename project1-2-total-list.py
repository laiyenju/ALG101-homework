# 範例輸入：[1, 2, 3]
# 範例輸出：6

array=list(map(int,input().split(","))) # 讓使用者輸入，並將輸入轉為 int
total = 0  #先設定總和為零

for i in range(len(array)):
    total = total + array[i]
print(total)
