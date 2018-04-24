#!/usr/bin/python

num = 0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            #print(i,j,k)
            if(i != j) and (i != k) and (j != k):
                num+=1
                print(i,j,k)

print(num)



