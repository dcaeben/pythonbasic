#hello first step 
a , b = 0 , 1 
while a < 1000: 
    print (a, end=(',')) # end evita el salto de linea y me permite una cadena diferente en este caso agrego la ,
    a, b = b, a + b 