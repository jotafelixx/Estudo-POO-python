

class Player:
    def __init__(self, nome):
        self.hp = 100
        self.name = nome
        self.dano = 20
        self.defesa = 10
        self.dinheiro = 0
    def mostrar_status(self):
        print(f'Nome:{self.name} \nHP:{self.hp} \nDano:{self.dano} \nDefesa:{self.defesa}\nDinheiro:{self.dinheiro}')
    def tomar_dano(self, danoInf):
        if danoInf < 0:
            print("O dano deverá que ser maior que 0.")
        else:
            danoMit = max(0, danoInf - self.defesa)
            self.hp -= danoMit
        if danoMit <= 0:
            print("Dano defendido totalmente!")
        print(f"Você tomou {danoMit} de dano! \nSeu HP atual é:{self.hp}")
    def atacar(self):
        return self.dano
       
