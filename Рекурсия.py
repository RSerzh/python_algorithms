ms = [2,7,4,5]

# Извращённое использование рекурсии для суммирования элементов массива
def rec_sum( ms , val=0 ):
    if len( ms )==0:
        return val
    else:
        val = val + ms.pop()
        return rec_sum( ms , val )

print( rec_sum( ms ) )
