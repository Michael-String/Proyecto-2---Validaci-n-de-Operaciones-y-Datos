# Proyecto 2: Longitud de una Frase
# UCamper: Michel Amir Madrigal Torres
# Bootcamp: Fundamentos de Python
# Coach: Gustavo Mota
# Grupo: C5

while(True):
  name = input("De favor ingrese una palabra: ")
  if len(name) < 4:
     print("Faltan letras")
  elif len(name) > 8:
     print("Sobran letras")
  else:
    break;

print("\nLa palabra es correcta: %s" % name)