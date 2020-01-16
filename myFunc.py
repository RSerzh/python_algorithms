# ver.16.01.20
# Функция генерации данных
import random as rnd
def get_data( size=100 ):
    rez=[]
    for i in range(1,size+1):
        rez.append( i )
    return rez