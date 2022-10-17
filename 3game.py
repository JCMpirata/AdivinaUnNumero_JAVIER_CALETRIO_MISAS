#Carpeta 3game

from 2start import(
2start.respuestaStartSiONo, 
2start.decidirNivel, 
2start.oportunidades
)

#Creo el codigo del juego
def juego(numero, minimo, maximo):
  intento = decidirNivel("Adivine el numero", minimo, maximo)
  
  if intento < numero:
    print("El numero que buscas es mas grande")
    minimo = intento + 1
    victoria = False
  elif intento > numero:
    print("El numero que buscas es mas pequeño")
    maximo = intento - 1
    victoria = False
  elif intento == oportunidades:
    victoria = False
    break
  else:
    print("Congratulations, you won")
    intento = minimo = maximo
    victoria = True
    return minimo, maximo, victoria
    
#Funcion para elegir nivel 
def eligirNivel(minimo,maximo):
  return decidirNivel("Elige un nivel", minimo,maximo)
  
#Funcion para jugar una partida  
def jugarPartida(numero, minimo, maximo):
  minimo,maximo,victoria = juego(numero, minimo, maximo)
  if(victoria):
  return

#Funcion para empezar a jugar
def jugar():
  minimo, maximo = decidirNivel()
  while True:
    numero = eligirNivel(minimo, maximo)
    jugarPartida(numero, minimo, maximo)
    if not respuestaStartSiONo("Nueva Partida: "):
      print("Goodbye")
      return
    
    
  
    


  
    
