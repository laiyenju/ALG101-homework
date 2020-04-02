list = [0, 0, 45, 6, 7, 100, -1]
min1 = list[0]
min2 = list[0]

for i in range(len(list)):  # 這裡以 len() 設定 list 長度範圍，避免直接使用 list 出現的 out of index 問題
    if list[i] < min1:
        min2 = min1
        min1 = list[i]
    elif list[i] < min2:
        min2 = list[i]
print(min1, min2)
