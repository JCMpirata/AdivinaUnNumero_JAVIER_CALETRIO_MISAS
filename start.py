import ramdom

respuestaStart = ("Si", "si", "Yes", "yes")
def respuestaStartSiONo():
  try:
    return input().lower() in respuestaStart
  except:
    return False

#Para elegir el nivel de partida creo la funcion 
def elegirNivel():
  nivel = "Elige el nivel de partida: "
  if nivel:
    Simple = radom.randint(0,100)
  elif:
    Intermedio = ramdom.randint(0,1000)
  elif:
    Avanzado = ramdom.randint(0, 1000000)
  else:
    Experto = ramdom.randint(0, 1000000000000)