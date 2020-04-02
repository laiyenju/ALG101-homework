import sys
str1 = sys.stdin.readline().strip('\n')
str2 = sys.stdin.readline().strip('\n')

num1 = int(str1)
num2 = int(str2)

def printable(num1, num2):
    for i in range(1, num1 + 1):
        for j in range(1, num2 + 1):
            result = i * j
            print("{}*{}={}".format(i, j, result))

printable(num1, num2)
