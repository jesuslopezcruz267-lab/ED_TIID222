#Declarando un arreglo
numeros = [10, 20, 30, 40, 50]

#Imprimimos un elemento en especial del arreglo
print(numeros[2])

#Reasigacion del valor de la posicion 

numeros[3] = 35
print(numeros)

#Se agrega un nuevo valor al final del arreglo
numeros.append(60)
print(numeros)


#Eliminamos un valor en el arreglo
numeros.remove(35)
print(numeros)


#Eliminamos un valor del arreglo usando la posición
numeros.pop(4)
print(numeros)


#

fruta = ['Manzana', 'Fresa', 'Sandía', 'Mango', 'Melon', 'Platano']

fruta.pop(4)
print(fruta)

fruta.remove('Manzana')
print(fruta)