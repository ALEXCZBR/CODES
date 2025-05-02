print("tabuada")

while True:
    num = int(input("Qual tabuada você quer saber? "))
    for n in range(0,11):
        resultado = num * n
        print(f"{num} X {n} = {resultado}")

#tabuada