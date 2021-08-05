import random


def play_oraculo():
      print('#######################')
      print('# Ask To Oráculo Game #')
      print('#######################')

      sequencia_numerica = random.randrange(0,101)
      numero_jogadas = 0
      points = 850

      print('Qual nível de dificuldade: ')
      print('(1) Fácil (2) Médio (3) Difícil')
      nivel = int(input('Selecione o grau de dificuldade: '))

      if nivel == 1:
        numero_jogadas = 17
      elif nivel == 2:
        numero_jogadas = 9
      else:
        numero_jogadas = 4

      for round in range(1, numero_jogadas + 1):
          print('Jogada {} de {}'.format(round, numero_jogadas))
          tentativa = int(input('Adivinhe a sequência numérica, digite um número:'))
          print('Você digitou:', tentativa)

          if tentativa < 1 or tentativa > 100:
            print('O número deve estar entre 1 e 100!')
            continue

          adivinhou = tentativa == sequencia_numerica
          numero_maior = tentativa > sequencia_numerica
          numero_menor = tentativa < sequencia_numerica

          if adivinhou:
              print('Adivinhou, parabéns!, Ganhou {} pontos'.format(points))
              break
          else:
              if numero_maior:
                  print('Sua sugestão foi maior do que a sequência numérica.')
              elif numero_menor:
                  print('Sua sugestão foi menor do que a sequência numérica.')
              print('Infelizmente, vocẽ não acertou.')
              lost_points = abs(sequencia_numerica - tentativa)
              points = points - lost_points
          print('----------------')
      print('Game Over!')


if __name__ == '__main__':
  play_oraculo()