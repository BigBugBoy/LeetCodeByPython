# -*- coding:UTF-8 -*-
# Author: bigbugboy
# Software: VS Code
# Datatime: 2018.12.19

def isPalindrome(x):
    if x==0: return True
    if x<0 or x%10 ==0 :return False
    else:
        palindrome = 0
        while(x > palindrome):
            palindrome = palindrome *10 + x % 10
            x = x//10
        return x == palindrome or x ==palindrome//10

if __name__ == '__main__':
    x = 0
    x = 1001
    print(isPalindrome(x))