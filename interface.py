from classes import Jogo21

class Interface():
  def __init__(self):
    self.jogo = Jogo21()

    sorteio = self.jogo.jogar_primeira_rodada() 

    print('Seu sorteio inicial foi:')
    print(sorteio[0])
    print(sorteio[1])

  def jogar_rodada(self):
    sorteio = self.jogo.jogar_rodada()

    print(f'A carta da rodada é {sorteio}')
    print(f'Sua pontuação é {self.jogo.pontuacao}')

  def continuar_rodada(self):
    if self.jogo.esta_encerrado():
      self.encerrar_jogo()
      return False

    escolha = input('Deseja continuar? Digite s para sim, outra tecla para encerrar')
    
    if escolha == 's':
      return True
    
    self.encerrar_jogo()
    return False

  def encerrar_jogo(self):
    print('Jogo encerrou. Sua pontuacao final é ' + str(self.jogo.pontuacao)) + '.'
