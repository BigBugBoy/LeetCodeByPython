# -*- coding:UTF-8 -*-
# Author: bigbugboy
# Software: VS Code
# Datatime: 2018.12.20

def RomanToInteger(s):
    le = len(s)
    R = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    result = 0
    i=0
    while(i<le):
        l = s[i]
        if i+1 == le:
            result = result + R[l]
            break
        r = s[i+1]
        if(R[l] < R[r]):
            result = result + R[r] -R[l]
            i=i+2
        else:
            result = result + R[l]
            i = i+1
    return result


if __name__ == '__main__':
    x = "D"
    print(RomanToInteger(x))