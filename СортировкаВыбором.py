import myFunc as mf

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

# Сортировка выбором с одним массивом
# и корректной сортировкой дублей
def sort2(dt):
    ln = len(dt)
    border = -1
    min = None
    for i in range(0,ln):
        for j in range(0,ln):
            if border >= j:
                continue
            val = dt[j]
            if min==None:
                min = val
                cur = border + 1
            else:
                if min >= val:
                    min = val
                    cur = j
        border +=1
        a1 = dt[cur]
        a2 = dt[border]
        dt[border] = a1
        dt[cur] = a2
        min=None

#rez = mf.get_random_arr( 16 )
rez = [ 55,3,3,1,0,1,2,6,9,11 ]
print( 'Исходные данные:' )
print( rez )
#print('------------')

# На выборке [ 55,3,3,1,0,1,2,6,9,11 ] sort1 вылетел с ошибкой. не справился
#sort1( rez )
print('------------')

# С дублями разбирается как надо
sort2( rez )
print( rez )
