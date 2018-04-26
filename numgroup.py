#!/usr/bin/python

# coding:utf-8

#需要优化，输入数字或者是字符串，都应该可以搞得定，类似于排列组合的一个东西

num = 0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            #print(i,j,k)
            if(i != j) and (i != k) and (j != k):
                num+=1
#                print(i,j,k)

#print(num)


#索引的使用，左侧包含边界，右侧不包含边界，-1则是从最右侧的元素开始

def perms(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in perms(elements[1:]):
           # print("aaaaa",perm)
           for i in range(len(elements)):
               yield perm[:i] + elements[0:1] + perm[i:]

for items in list(perms([1,2,3,4])):
    print(items)
    











