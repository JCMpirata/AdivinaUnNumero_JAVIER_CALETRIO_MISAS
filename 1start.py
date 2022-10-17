from 2niveles import
nivel_simple,nivel_intermedio,nivel_avanzado,nivel_experto

"Creo la funcion respuestaStartSiONo para crear las diferentes respuestas validas para (Nueva partida: )"
def respuestaStartSiONo():
  respuestaStart = ("Si", "si", "Yes", "yes")
  try:
    return input().lower() in respuestaStart
  except:
    return False
    
#Creo la funcion decidir nivel, en la cual explico los diferentes niveles y utilizo un condicional para eligir el nivel en el que quiero jugar. A la hora de elegir un nivel, importo las funciones creadas en la carpeta 2niveles.py y las utilizo para jugar a adivinar un numero aleatorio comprendido entre el minimo y el maximo de ese nivel. 
def decidirNivel():
  while True:
    print("1 - Nivel Simple(de 0 a 100)" )
    print("2 - Nivel intermedio(de 0 a 1000")
    print("3 - Nivel Avanzado(de 0 al 1000000")
    print("4 - Nivel Experto(de 0 a 1000000000000")
    respuestaNivel = input("Elige un nivel: ")
    if respuestaNivel == "1":
      nivel_simple()
    elif respuestaNivel == "2":
      nivel_intermedio()
    elif respuestaNivel == "3":
      nivel_avanzado()
    elif respuestaNivel =="4":
      nivel_experto()
    else:
      print("Error")
      return decidirNivel()
      
