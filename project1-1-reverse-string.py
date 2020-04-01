# 1. 給一個字串 str，請輸出 str 反過來的結果
# 範例輸入：hello
# 範例輸出：olleh

# PS. 可以用 str[i] 取得第 i 個字，例如說 str="abc"，str[0] 就是 'a'

str = input("pleas enter a word\n") # 讓使用者輸入字串
new_str = ""  #建立空字串

for i in range(len(str)-1):
    new_str = new_str + str[-(i+1)]  # 倒著數字串（避開第0序列）
new_str = new_str + str[0] # 補上第0序列
print(new_str)
