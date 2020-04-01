# 3. 找最大值
# 給一個陣列 arr，裡面全都包含了數字（整數），請輸出陣列中的最大值

# 範例輸入：[1, 2, 3]
# 範例輸出：3

array=list(map(int,input().split(",")))
largest = array[0]

for i in range(len(array)):
    if array[i] > largest:
        largest = array[i]
print(largest)
