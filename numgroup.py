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


#给定4个数全排列的递归算法实现，
#4个数全排列其实等于3个数全排列的可能性再加上1个数插到所有位置，
#依次类推，运用yield的记忆属性，可以实现全排列收集
def perms(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in perms(elements[1:]):
           # print("aaaaa",perm)
           for i in range(len(elements)):
               #print("bbbbbb",i,perm[:i],elements[0:1],perm[i:])
               yield perm[:i] + elements[0:1] + perm[i:]

for items in list(perms([1,2,3,4])):
    print(items)
    











