arreglo = [1, 8, 27, 65, 125]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
lista = []
def listas(lista):
   cube = 4 ** 3
   lista[3] = cube #remplazamos el valor en la pocisión 3 
   lista.append(216) # la función append agrega un valor al final de la lista 
   lista.append(7 ** 3) # tambien podemos agregar una operación

   return lista 

def listasMore(lista):
    lista[2:5] = ['C', 'D', 'E'] # remplazando valores asignando pocisiones 
    
    return lista

def contentLista(a,b):
    lista = [a, b] # una lista conteniendo otras listas

    return lista 

print (listas(arreglo))
print (listasMore(letters))
print (contentLista(arreglo, letters))