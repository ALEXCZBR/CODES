horas = float(input("Que horas são? "))

if horas >=6 and horas <= 11:
    print("Bom dia!!")
elif horas >= 12 and horas <= 18:
    print("Boa tarde!!")
elif horas >= 19 and horas <= 23:
    print("Boa noite!!")
else:
    print("Boa madrugada!!")

#Relógio