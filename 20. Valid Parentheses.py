# -*- coding:UTF-8 -*-
# Author: bigbugboy
# Software: VS Code
# Datatime: 2018.12.13

def cp(s1, s2):
    if s1 =="[" and s2 =="]":return True
    if s1 =="{" and s2 =="}":return True
    if s1 =="(" and s2 ==")":return True
    else: return False

def isValid(s):
    l=[]
    if len(s) ==0: return True
    if len(s) ==1: return False
    l.append(s[0])
    s = s[1:]
    cpp = {"(":")", "[":"]", "{":"}"}
    for i in range(len(s)):
        if(len(l)>0 and (l[len(l)-1] in cpp) and cpp[l[len(l)-1]] == s[i]):
            l.pop()
        else:
            l.append(s[i])
    return not l

if __name__ == "__main__":
    s = "([)]"
    print(isValid(s))