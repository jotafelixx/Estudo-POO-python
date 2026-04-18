from player import Player
from enemy import Inimigo
nome_jogador = input("Digite seu nome: ")
print(f"Olá, seja bem-vindo e divirta-se.\n" )
inimigo = Inimigo()
jogador = Player(nome_jogador)
jogador.mostrar_status()
inimigo.mostrar_status()
acao = 1

    
while acao == 1:
    acao = int(input("\n--- NOVO TURNO ---\n1 - Atacar\n 2 - Fugir\n"))   
    if acao != 1 and acao != 2:
        print("Digite uma das ações!")
        continue
    if acao == 2:
        break
    elif acao == 1:
        dano = jogador.atacar()
        inimigo.tomar_dano(dano)
    if inimigo.hp <= 0:
        jogador.dinheiro += inimigo.recompensa
        print(f'Você matou o inimigo de nivel {inimigo.nivel} e foi adicionado {inimigo.recompensa} na sua carteira você tem {jogador.dinheiro} agora!')
    else:
        dano_inimigo = inimigo.atacar()
        jogador.tomar_dano(dano_inimigo)
  
    if jogador.hp <= 0:
        print("Você perdeu!:(")
        break


    
