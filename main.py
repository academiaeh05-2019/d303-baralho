from classes import Carta, Baralho


carta1 = Carta('Paus', 'As', 1)
carta2 = Carta('Copas', 'Rei', 10)
carta3 = Carta('Espadas', 'Cinco', 5)
baralho = Baralho()

print(baralho)
baralho.adicionar_carta(carta1)
baralho.adicionar_carta(carta2)
baralho.adicionar_carta(carta3)
print(baralho)
print(baralho.remover_carta())

