from 1start import(
respuestaSiONo,
decidirNivel
) 

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
  else:
    print("Congratulations, you won")
    intento = minimo = maximo
    victoria = True
    return minimo, maximo, victoria
    
def eligirNivel(minimo,maximo):
  return decidirNivel("Elige un nivel", minimo,maximo)
  
def jugarPartida(numero, minimo, maximo):
  minimo,maximo,victoria = juego(numero, minimo, maximo)
  if(victoria):
  return
  
def jugar():
  minimo, maximo = deicirNivel(level)
  while True:
    numero = eligirNivel(minimo, maximo)
    jugarPartida(numero, minimo, maximo)
    if not respuestaStartSiONo("Nueva Partida: "):
      print("Adios")
      return
    
    
  
    


  
    
