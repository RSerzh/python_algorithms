from myFunc import get_data

# Моя функция
def seek( dt, val, debug=False):
    if (val not in dt):
        print('Значения нет в списке')
        return None

    lim = 5000
    ln = len(dt)
    curA = round( ln/2 )
    curB = ln
    get_val = dt[curA-1]
    i = 1
    while get_val != val:
        if( get_val > val):
            curB = curA
            curA = round(curA/2)
        else:
            dlt = curB - curA
            if dlt==1:
                curA = curA + dlt
            else:
                curA = curA + round( (dlt) / 2 )
        get_val = dt[curA-1]

        i +=1
        if( i > lim):
            print(f'Количество итераций поиска большое ({lim}). Похоже на бесконечный цикл. Прерываем.')
            return None
        if( get_val == val):break

    print( 'Итерация =' , i )
    print( 'Позиция №' , curA - 1 )

# Второй вариант функции
# Всё равно работает не оптимально для 50 000 должно быть не более 16 - 20
# итераций, а бывает под 50
# Но для знакомства с бинарным поиском думаю будет достаточно
def seek2( dt, val):
    if (val not in dt):
        return 'Not in list'
    print('Ищем:' , val)
    right = len(dt)-1
    left = round(right/2)
    get_val = dt[left]

    print( left , right , f'get_val={get_val}' )
    lim = 500
    i = 1
    while get_val != val:
        i += 1 # Подсчёт итераций

        if get_val > val:
            right = left
            left = round(left/2)
            sign = '>'
        else:
            left = left + round( (right - left) / 2) + i%2
            # Финт с остатком от деления даёт либо 0 либо 1
            # Помогает решить проблему установки указателя
            sign = '<'

        get_val = dt[left]
        print( left , right , f'get_val={get_val} {sign}'  )
        lim -=1
        if lim==0:
            break

    print('Итераций =', i , " Позиция =" , left)
    return get_val

# Как автор рекомендует в учебнике
# Но как то странно получается. Этот алгоритм тупо перебирает поочереди
# Нет никакого деления. Наверняка какая то ошибка
def book_seek( list , item ):
    low = 0
    high = len( list ) - 1

    # мой счетчик для подсчета итераций
    i = 0

    while low <= high :
        i += 1
        mid = ( low + high )
        guess = list[mid]
        if guess == item:
            print( 'Итераций =' , i )
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

rez = get_data( 50000 )
print("Используем массив rez:")
#print( rez )
print('-----')
# print('\nАлгоритм book_seek ')
# print( 'позиция № ' , book_seek( rez , 62 ) )

# print('\nАлгоритм seek ')
# seek( rez , 62 )

print( seek2( rez , 48001 ) )
