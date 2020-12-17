
#Cuenta regresiva : crea una función que acepte un número como entrada. Devuelve una nueva lista que cuenta
# hacia atrás en uno, desde el número (como el elemento 0) hasta 0 (como el último elemento).
#Ejemplo: la cuenta regresiva (5) debería devolver [5,4,3,2,1,0]

def ctaRegresivaX4():
    print('Ha iniciado función cuenta regresiva. \n')
    num=input('Ingrese un numero para realizar la cuenta regresiva: ')
    num=int(num)
    list=[]
    for x in range (num,-1,-1):
        list.append(x)
    print(list)

#Imprimir y volver : crea una función que recibirá una lista con dos números.
#Imprima el primer valor y devuelva el segundo.
#Ejemplo: print_and_return ([1,2]) debería imprimir 1 y devolver 2

def printAndReturn(lista):
    print('\nHa iniciado la función printAndReturn. \n')
    print(lista[0])
    return lista[1]

#First Plus Length : crea una función que acepta una lista y devuelve la suma
# del primer valor de la lista más la longitud de la lista.
#Ejemplo: first_plus_length ([1,2,3,4,5]) debería devolver 6 (primer valor: 1 + longitud: 5)

def firstPlussLenght(lista):
    print('\nHa iniciado la función firstPlussLenght. \n')
    return lista[0] + len(lista)

#Valores mayores que el segundo : escribe una función que acepte una lista y
# crea una nueva lista que contenga solo los valores de la lista original que sean mayores que su segundo valor.
# Imprima cuántos valores son y luego devuelva la nueva lista. Si la lista tiene menos de 2 elementos,
# haga que la función devuelva False
#Ejemplo: values_greater_than_second ([5,2,3,2,1,4]) debería imprimir 3 y devolver [5,3,4]
#Ejemplo: values_greater_than_second ([3]) debería devolver False

def values_greater_than_second(lista):
    print('\nHa iniciado la función values_greater_than_second. \n')
    new_list = []
    if len(lista)<2:
        return False
    else:
        for x in range (0,len(lista),1):
            if x==1:
                continue
            if lista[x]>lista[1]:
                new_list.append(lista[x])
        print('El largo de la lista es:', len(new_list))
    return new_list

#Esta longitud, ese valor : escribe una función que acepte dos enteros como parámetros: tamaño y valor.
# La función debe crear y devolver una lista cuya longitud es igual al tamaño dado
# y cuyos valores son todos los valores dados.
#Ejemplo: length_and_value (4,7) debería devolver [7,7,7,7]
#Ejemplo: length_and_value (6,2) debería devolver [2,2,2,2,2,2]

def creandoLista():
    print('\nHa iniciado la función creandoLista. \n')
    tam=input('Ingrese tamaño de la lista: ')
    valor=input('Ingrese valor de la lista: ')
    tam=int(tam)
    valor=int(valor)
    lista=[]
    for x in range (0,tam,1):
        lista.append(valor)
    print(lista)






if __name__ == '__main__':
    ctaRegresivaX4()
    printAndReturn([1,2])
    print('La suma entre el primer valor de la lista y su longitud es:', firstPlussLenght([1,2,3,4,5]))
    print('La función ha devuelto:', values_greater_than_second([5,2,3,2,1,4]))
    print('La función ha devuelto:', values_greater_than_second([3]))
    creandoLista()

