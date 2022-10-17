
def respuestaStartSiONo():
  respuestaStart = ("Si", "si", "Yes", "yes")
  try:
    return input().lower() in respuestaStart
  except:
    return False
    
def decidirNivel():
  print("1 - Nivel Simple(de 0 a 100)" )
  print("2 - Nivel intermedio(de 0 a 1000")
  print("3 - Nivel Avanzado(de 0 al 1000000")
  print("4 - Nivel Experto(de 0 a 1000000000000")
  respuestaNivel = input("Elige un nivel: ")
  while True:
    if respuestaNivel == "1":
      import nivel_simple
    elif respuestaNivel == "2":
      import nivel_intermedio
    elif respuestaNivel == "3":
      import nivel_avanzado
    elif respuestaNivel =="4":
      import nivel_experto
    else:
      print("Error")
      return decidirNivel()
      
