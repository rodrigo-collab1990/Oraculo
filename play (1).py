import forca
import oraculo

print('#################')
print('# Selecione um Jogo #')
print('#################')

print('(1) Forca  (2) Oráculo')

game = int(input("> "))

if game == 1:
  print('forca')
  forca.play_forca()
elif game == 2:
  print('oraculo')
  oraculo.play_oraculo()