import ramdom

def respuestaStartSiONo():
  respuestaStart = ("Si", "si", "Yes", "yes")
  try:
    return input().lower() in respuestaStart
  except:
    return False

def elegirNivel():
  nivel = "Elige el nivel de partida: "
  if nivel:
    Simple = radom.randint(0,100)
  elif nivel:
    Intermedio = ramdom.randint(0,1000)
  elif nivel:
    Avanzado = ramdom.randint(0, 1000000)
  else:
    Experto = ramdom.randint(0, 1000000000000)