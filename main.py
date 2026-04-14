from player import Player
from enemy import Inimigo
nome_jogador = input("Digite seu nome: ")
print(f"Olá, seja bem-vindo e divirta-se.\n" )
inimigo = Inimigo()
jogador = Player(nome_jogador)
jogador.mostrar_status()
inimigo.mostrar_status()
while jogador.hp > 0 and inimigo.hp > 0:
    print("\n--- NOVO TURNO ---")
    dano = jogador.atacar()
    dano_inimigo = inimigo.atacar()
    inimigo.tomar_dano(dano)
    jogador.tomar_dano(dano_inimigo)
if inimigo.hp <= 0:
    jogador.dinheiro += inimigo.recompensa
    print(f'Você matou o inimigo de nivel {inimigo.nivel} e foi adicionado {dinheiro} na sua carteira você tem {carteira} agora!')
elif jogador.hp == 0:
    print("Você perdeu!:(")

