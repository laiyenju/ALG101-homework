# 2. 陣列總和
# 給一個陣列 arr，裡面全都包含了數字（整數），請輸出陣列加總的結果（總和保證不超過 int 範圍）

# 範例輸入：[1, 2, 3]
# 範例輸出：6

array=list(map(int,input().split(","))) # 讓使用者輸入，並將輸入轉為 int
total = 0  #先設定總和為零

for i in range(len(array)):
    total = total + array[i]
print(total)
