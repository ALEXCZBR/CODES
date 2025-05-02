frutas = ('maçã', 'banana', 'laranja', 'uva')

if 'banana' in frutas:
    print("banana em frutas")
lista_frutas = list(frutas)
lista_frutas.append('abacaxi')
frutas = tuple(lista_frutas)
print(frutas)

#lista de frutas