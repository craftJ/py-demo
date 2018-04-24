
import time

words = input("here is sth for your special \"one\":")

def heartfunc(x,y):
    if (((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0):
        return True
    else:
        return False

for item in words.split():
    print('\n'.join([''.join([item[(x-y) % len(item)] if heartfunc(x,y) else ' ' for x in range(-40,40,1)]) for y in range(15,-15,-1)]))
    time.sleep(1.5)
