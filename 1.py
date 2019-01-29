#!/usr/bin/python
# -*- coding: UTF-8 -*-

#有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

r=[]
e=[]
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i!=j) and (j!=k) and (k!=i):
                
                r.append([i,j,k])
            else:
                e.append(f'{i}{j}{k}')

print('无重复数字：',len(r))
print('有重复数字：',len(e))
print(e)

