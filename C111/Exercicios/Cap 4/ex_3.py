import numpy as np

campo = np.zeros((2, 2), dtype=int)

linha_bomba = np.random.randint(0, 2)
coluna_bomba = np.random.randint(0, 2)
campo[linha_bomba][coluna_bomba] = 1

print("Mini Campo Minado 2x2")

tentativas = 0
acertos = 0

while tentativas < 3:
    print("\nDigite a posição (linha e coluna entre 0 e 1)")
    linha = int(input("Linha: "))
    coluna = int(input("Coluna: "))
    
    tentativas += 1
    
    if campo[linha][coluna] == 1:
        print("Game Over! :( Try Again!")
        break
    else:
        acertos += 1
        print("Posição segura!")
        
        if acertos == 3:
            print("Congratulations! You beat the game! :)")
            break