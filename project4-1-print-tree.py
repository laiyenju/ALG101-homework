import sys
str = sys.stdin.readline().strip('\n')
num = int(str)

# 印出樹葉的寫法
def star(i):
    return (2 * i + 1) * "*"

# 印出空格的寫法
def space(i):
    return (num - 1 - i) * " "

# 印出樹幹的寫法
def stick(i):
    return (num - 1) * " " + "|"

# 將前三項組合起來
def tree(num):
    for i in range(num):  # 先將樹葉跟空格印出來後
        print(space(i) + star(i))

    for i in range(1, num):  # 再印出樹幹
        print(stick(i))

tree(num)
