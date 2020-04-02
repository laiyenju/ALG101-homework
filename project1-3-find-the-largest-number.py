# 範例輸入：[1, 2, 3]
# 範例輸出：3

array=list(map(int,input().split(",")))
largest = array[0]

for i in range(len(array)):
    if array[i] > largest:
        largest = array[i]
print(largest)
