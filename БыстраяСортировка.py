from random import *
from time import time
import myFunc as myF

# Быстрая сортировка Хоара
def quick_sort( ms ):
    if len(ms)>1:
        pv = choice(ms)
        left = [ x for x in ms if x < pv]
        mid = [ x for x in ms if x == pv]
        right = [ x for x in ms if x > pv]
        return quick_sort(left) + mid + quick_sort(right)
    else:
        return ms

# Сортировка слиянием
def merge(a,b):
    i = 0
    j = 0
    rezult = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            rezult.append(a[i])
            i+=1
        else:
            rezult.append(b[j])
            j+=1
    rezult += a[i:] + b[j:]
    return rezult

def merge_sort(a):
    if len(a) > 1:
        a1 = merge_sort( a[ : len(a) // 2 ] )
        a2 = merge_sort( a[ len(a) // 2 : ] )
        return merge( a1 , a2 )
    else:
        return a

ms = [2,4,3,1,9,3,2,5,8,1,6,7]
#ms = myF.get_random_arr( 20 )

print('Исходные данные :' , ms)
ms = quick_sort(ms)
print(ms)
ms = merge_sort(ms)
print(ms)
