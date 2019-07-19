class Carta():
  def __init__(self, naipe, rank, valor):
    self.naipe = naipe
    self.rank = rank
    self.valor = valor

  def __str__(self):
    return f'{self.rank} de {self.naipe} [{self.valor}]'

class Baralho():
  def __init__(self):
    self.cartas = []

  def __str__(self):
    if len(self.cartas) == 0:
      return '[VAZIO]' 

    string = ''
    
    for carta in self.cartas:
      string += str(carta)
      string += ', '

    return string

  def adicionar_carta(self, carta):
    self.cartas.append(carta)

  def remover_carta(self):
    return self.cartas.pop()
