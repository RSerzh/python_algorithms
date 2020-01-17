import myFunc as fnc
import time as tm

# По сути декоратор для тестирования функций
def tst( fname , i ):
    start = tm.time()
    ms = fname( i )
    end = tm.time()
    print( 'Время работы =' , end - start )
    
iterations = 1000 * 1000 * 100
tst( fnc.get_data , iterations )
tst( fnc.get_data2 , iterations )