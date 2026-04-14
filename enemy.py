from random import randrange

class Inimigo:
    def __init__(self):
        self.nivel = randrange(1, 3)
        self.bonusNivel = 5 * self.nivel
        self.hp = 100 + self.bonusNivel
        self.recompensa = 10 * self.nivel
        self.defesa = 10 + self.bonusNivel
        self.dano = 10 + self.bonusNivel
    def mostrar_status(self):
        print(f'Nivel:{self.nivel} \nHP:{self.hp} \nDano:{self.dano} \nDefesa:{self.defesa}')
    def tomar_dano(self, danoInf):
        if danoInf < 0:
            print("O dano deverá que ser maior que 0.")
        else:
            danoMit = max(0, danoInf - self.defesa)
            self.hp -= danoMit
        if danoMit <= 0:
            print("Dano defendido totalmente!")
        print(f"Inimigo tomou {danoMit} de dano! \nHP atual é:{self.hp}")
    def atacar(self):
        return self.dano