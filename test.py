#!/usr/bin/python3
#_*_ coding:UTF-8 _*_
print('hello word')
name=input('请输入你的名字：')
print(name)
i=1
while i<=9:
  j=1
  while j<=i:
    print('%d*%d=%d\t'%(j,i,j*i),end="")
    j+=1
  i+=1
