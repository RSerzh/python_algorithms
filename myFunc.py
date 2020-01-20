# ver.18.01.20
# Функция генерации данных
import random as rnd

def fill_cell():
    return rnd.randint(0,10)

#динамическое  с вызовом функции
def get_data( size=100 ):
    rez=[]
    for i in range(0,size+1):
        rez.append( i )
    #print( "-ДФ" )
    return rez
