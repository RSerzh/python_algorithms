import myFunc as mf

rez = mf.get_random_arr( 25 )
#rez = [ 0,3,3,1,2,6,9,11 ]
print( 'Исходные данные:' )
print( rez )
print('------------')

# Сортировка выбором что сразу пришло в голову
# Но проблема, если встречаются дубли значений
def sort1(dt):
    ln = len(dt)
    rez = [0] * ln
    min = -1
    for i in range( 0 , ln ):
        cur = None
        for j in range( 0 , ln ):
            val = dt[j]
            if min >= val:
                continue
            if cur==None:
                cur = val
            else:
                if cur > val:
                    cur = val
        min = cur
        rez[i] = cur
    print(rez)
sort1( rez )

#dt = myFunc.get_random_arr()
