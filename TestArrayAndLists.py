import myFunc as fnc
import time as tm
import random as rnd

# По сути декоратор для тестирования функций
def tst( fname , i=20 ):
    start = tm.time()
    ms = fname( i )
    end = tm.time()
    print( 'Время работы =' , end - start )
    return ms

iterations = 1000 * 1000 * 10
#iterations = 1000 * 1000 * 2
print("Заполнение массива данными:")

# tst( fnc.get_data , iterations )
# tst( fnc.get_data2 , iterations )
ms1 = tst( fnc.get_data3 , iterations )
ms2 = tst( fnc.get_data4 , iterations )
ms3 = tst( fnc.get_data5 , iterations )
print(len(ms3))
