from player import Player
nome_jogador = input("Digite seu nome: ")
print(f"Olá, seja bem-vindo e divirta-se.\n" )

jogador = Player(nome_jogador)
while jogador.hp > 0:
    jogador.mostrar_status()
    jogador.tomar_dano(1)