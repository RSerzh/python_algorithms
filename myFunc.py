# ver.17.01.20
# Функция генерации данных
import random as rnd

def fill_cell():
    return 0
    return rnd.randint(0,10)

#динамическое  с вызовом функции
def get_data( size=100 ):
    rez=[]
    for i in range(1,size+1):        
        rez.append( fill_cell() )
    print( "-ДФ" )
    return rez

#статическое с вызовом функции
def get_data2( size=100 ):
    rez=[0]*size
    
    for i in range(1,size):
        rez[i]=fill_cell()
    
    print( "-CФ" )
    return rez

#динамическое без вызова функции
def get_data3( size=100 ):
    rez=[]
    
    for i in range(1,size):
        rez.append( 9 )
    
    print( "-Д" )
    return rez

#статическое без вызова функции
def get_data4( size=100 ):
    rez=[0]*size
    
    for i in range(1,size):
        rez[i]=9
    
    print( "-С" )
    return rez