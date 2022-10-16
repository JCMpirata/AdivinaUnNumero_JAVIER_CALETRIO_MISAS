import random

def decidirNivel(level):
  while True:
    level = ("Elige un nivel: ")
    if level:
      Simple = radom.randint(0,100)
    elif level:
      Intermedio = ramdom.randint(0,1000)
    elif level:
      Avanzado = ramdom.randint(0, 1000000)
    else:
      Experto = ramdom.randint(0, 1000000000000)
    return elegirNivel(level)
   

    