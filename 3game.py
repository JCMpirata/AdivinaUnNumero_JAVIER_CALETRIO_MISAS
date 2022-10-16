from start import(
  respuestaStartSiONo,
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
    print("Enhorabuena, el numero era {numero}")
    intento = minimo = maximo
    victoria = True
    return minimo, maximo, victoria
    
def elirNivel(minimo,maximo):
  return Nivel("Elige un nivel", minimo,maximo)
  
def jugarPartida(numero, minimo, maximo):
  minimo,maximo,victoria = juego(numero, minimo, maximo)
  if(victoria):
  return
  
def jugar():
  minimo, maximo = deicirNivel(level)
  while True:
    numero = decirNivel(level)
    jugarPartida(numero, minimo, maximo)
    if not respuestaStartSiONo("Nueva Partida: "):
      print("Adios")
      return
    
    
  
    


  
    
