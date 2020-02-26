# traigo Pin de machine para poder obtener una instancia de ledazul (que es el pin 2)
from machine import Pin

# traigo time porque lo voy a usar para el sleep del parpadeo
import time

# defino ledazul como el pin 2 y lo configuro como salida
ledazul = Pin(2, Pin.OUT)

# apago el led azul
ledazul(0)

# enciendo el led azul
ledazul(1)

# itero un rango de 10 elementos
for i in range(10):
  # seteo el value de led azul con el resto a dos del valor iterado (va a ser 0 o 1)
  ledazul.value(i%2)
  #  hago un sleep de 1 segundo
  time.sleep(1)

#defino una función toggle que recibe un parámetro p (idealmente class Pin)
def toggle(p):
  # seteo el value de p como el valor actual negado
  p.value(not p.value())

# itero un rango de 10 elementos
for i in range(10):
  # ejecuto la función toggle pasándole ledazul como parámetro
  toggle(ledazul)
  # hago un sleep de 100ms
  time.sleep(0.1)