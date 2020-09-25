import numpy as np
def eliminar_menor (cod: str, a: int, b: int, c: int, d: int, e: int):
      arrb = [a, b, c, d, e]
      resul = []
      arr =np.array([a, b, c, d, e])
      menor = np.amin(arr) # devuelve el minimo valor 

      arrb.remove(menor) # devuelve el valor del arreglo sin el menor valor

      promedio = ((arrb[0] + arrb[1] + arrb[2] + arrb[3]) / 4) # aqui estaba el error por parentesis

      promedio = (promedio / 20)

      promedio = round(promedio,2)

      return "el promedio del ajustado del estudiante " + cod + " es : " + str(promedio)

print (eliminar_menor('10299093D', 19, 90, 38, 55, 68))
print (eliminar_menor('10299093D', 37, 10, 50, 19, 79))
print (eliminar_menor('10299093D', 45, 46, 33, 74, 22))
print (eliminar_menor('10299093D', 57, 100, 87, 93, 21))
print (eliminar_menor('10299093D', 5, 14, 76, 91, 5))

