# -*- coding:UTF-8 -*-
# Author: bigbugboy
# Software: VS Code
# Datatime: 2018.12.19

def reverse(x):
    x = int(x)
    y = 0
    if(x == 0): y = x
    if(x>0):
        s = str(x)
        y = s[::-1]
    if(x<0):
        s = str(x)
        z = s[1:]
        y = "-" + z[::-1]
    y = int(y)
    if(y<-2**31 or y>2**31-1):return 0
    else:return y

if __name__ == '__main__':
    x = input("请输入要测试的数字")
    # print(2**31-1)
    # x = 1534236469
    print(reverse(x))