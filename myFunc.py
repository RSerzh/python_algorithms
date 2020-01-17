# ver.17.01.20
# Функция генерации данных
import random as rnd
def get_data( size=100 ):
    rez=[]
    for i in range(1,size+1):        
        rez.append( 7 )
    print( "Динамическое заполнением массива" )
    return rez

def get_data2( size=100 ):
    rez=[0]*size
    
    for i in range(1,size):
        #rez.append( 7 )
        rez[i]=7
    
    print( "Статическое заполнение массива" )
    return rez