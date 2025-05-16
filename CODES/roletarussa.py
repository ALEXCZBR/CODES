import random
import time

def roleta_russa():
    print("Bem-vindo à Roleta Russa!")
    print("Girando o tambor...")
    time.sleep(2)

    # Define a posição da bala no tambor (1 a 6)
    bala = random.randint(1, 6)
    print("O tambor está pronto. Boa sorte!\n")

    # Jogador escolhe uma posição
    tentativa = int(input("Escolha um número de 1 a 6: "))

    if tentativa == bala:
        print("Bang! Você perdeu!")
    else:
        print("Clique! Você sobreviveu!")

if __name__ == "__main__":
    roleta_russa()