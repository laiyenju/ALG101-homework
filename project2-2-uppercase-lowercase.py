# 讓使用者輸入字串
words = input("type a word\n")

# 先假設大小寫轉換完的字串
transformed_words = ""

# pseudocode
# 如果 ord(words[i]) 介於 65-90 間，表示是大寫
#     ord(words[i]) + 32，轉換成小寫的 ascii code 數字
#     使用 chr() 將 ascii code 轉換成字串
# 如果 ord(words[i]) 介於 97-122 間，表示是小寫
#     ord(words[i]) - 32，轉換成大寫的 ascii code 數字
#     使用 chr() 將 ascii code 轉換成字串


for i in range(len(words)):
    if ord(words[i]) >= 65 and  ord(words[i]) <= 90:
        new_ascii_code = ord(words[i]) + 32
        transformed_word = chr(new_ascii_code)
        transformed_words = transformed_words + transformed_word
    elif ord(words[i]) >= 97 and  ord(words[i]) <= 122:
        new_ascii_code = ord(words[i]) - 32
        transformed_word = chr(new_ascii_code)
        transformed_words = transformed_words + transformed_word
print(transformed_words)
