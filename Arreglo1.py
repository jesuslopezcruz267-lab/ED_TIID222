n = 15

arreglo = [0] * n

for i in range(n):
    dato = int(input('Ingrese un número entero comprendido entre 0 y 500: '))

    while dato < 0 or dato > 500:
        print('Error: el número debe estar entre 0 y 500.')
        dato = int(input('Ingrese un número entero comprendido entre 0 y 500: '))

    arreglo[i] = dato

print('\nArray original:')
for num in arreglo:
    print(num, end=' ')

cincuerizado = []

for num in arreglo:
    if num % 5 == 0:
        cincuerizado.append(num)
    else:
        siguiente_multiplo = num + (5 - num % 5)
        cincuerizado.append(siguiente_multiplo)

print('\n\nArray cincuerizado:')
for num in cincuerizado:
    print(num, end=' ')