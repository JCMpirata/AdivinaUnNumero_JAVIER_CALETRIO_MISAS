#Carpeta 2sart

from 1niveles import(
1niveles.nivel_simple,
1niveles.nivel_intermedio,
1niveles.nivel_avanzado,
1niveles.nivel_experto
)

"Creo la funcion respuestaStartSiONo para crear las diferentes respuestas validas para (Nueva partida: )"

#Funcion para obtener una respuesta a "Nueva partida: " la cual utilizare esta funcion en la carpeta 3game
def respuestaStartSiONo():
  respuestaStart = ("Si", "si", "Yes", "yes")
  try:
    return input().lower() in respuestaStart
  except:
    return False
    
#Creo la funcion decidir nivel, en la cual explico los diferentes niveles y utilizo un condicional para eligir el nivel en el que quiero jugar. A la hora de elegir un nivel, importo las funciones creadas en la carpeta 2niveles.py y las utilizo para jugar a adivinar un numero aleatorio comprendido entre el minimo y el maximo del nivel elegido.
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

#Creo la funcion oportunidades, haciendo que el maximo numero de oportunidades que tiene el jugador para adivinar el numero son 5.

def oportunidades():
  numIntentos = 0
  while True:
    oportunidades = numIntentos + 1
  if oportunidades <= 5:
    print("Sigue intentandolo")
  else:
    print("Game over")
  return oportunidades
#Creo la funcion puntuaciones, en la que creo un diccionario vacio para finalmente introducir el nombre del jugador y la puntuacion en el diccionario al imprimirlo. Para la puntuacion utilizo un condicional para dar las diferentes puntuaciones que puede obtener el jugador dependiendo del numero de oportunidades que ha usado para adivinar el numero.
def puntuaciones():
  tabla = {}
  tabla["nombreJugador"] = input("Introduce un nombre: ")
  tabla["puntuacion"] = puntuacion
  puntos = 0
  if oportunidades == 1:
    puntuacion = puntos + 100
  elif oportunidades == 2:
    puntuacion = puntos + 50
  elif oportunidades == 3:
    puntuacion = puntos + 25
  elif oportunidades == 4:
    puntuacion = puntos + 10
  elif oportunidades == 5:
    puntuacion = puntos + 5
  else:
    puntuacion = 0

  print tabla["nombreJugador", "puntos"]
  return tabla

  
