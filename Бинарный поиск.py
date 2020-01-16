from myFunc import get_data

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
        
        if(debug):
            print( f'={get_val}' )
        
        if( get_val > val):
            if(debug):
                print( f' > curA={curA} curB={curB} ' )
            curB = curA
            curA = round(curA/2)
            if(debug):
                print( f' >2 curA={curA} curB={curB} ' )
            
        else:
            
            dlt = curB - curA
            if dlt==1:
                curA = curA + dlt
            else:
                curA = curA + round( (dlt) / 2 )
            
            if(debug):
                print( f' < curA={curA} curB={curB} (dlt){dlt}' )
            
        get_val = dt[curA-1]
        
        i +=1
        if( i > lim):
            print(f'Количество итераций поиска большое ({lim}). Похоже на бесконечный цикл. Прерываем.')
            return None
        if( get_val == val):break

    if(debug):
        print('-----')
    print(f'Результат = {get_val} за {i} итераций' )

rez = get_data( 56 )
print("Используем массив rez:")
print(rez)
seek( rez , 7 )