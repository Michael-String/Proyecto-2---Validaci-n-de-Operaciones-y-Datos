# Proyecto 2: Encuentra el Cuadrante
# UCamper: Michel Amir Madrigal Torres
# Bootcamp: Fundamentos de Python
# Coach: Gustavo Mota
# Grupo: C5


# Ubicación de Cuadrantes en el Plano Cartesiano

x, y = map(int, list(input("De favor ingrese un valor para variable X y Y : ").split(" ")))

# Condición del Cuadrante I 
if x > 0 and y > 0:
    print("El punto (", x, ",", y, ") se encuentra en el Cuadrante I")

# Condición del Cuadrante II 
elif x < 0 and y > 0:
    print("El punto (", x, ",", y, ") se encuentra en el Cuadrante II")

# Condición del Cuadrante III 
elif x < 0 and y < 0: 
    print("El punto (", x, ",", y, ") se encuentra en el Cuadrante III")
    
 # Condición del Cuadrante IV
elif x > 0 and y < 0:
    print("El punto (", x, ",", y, ") se encuentra en el Cuadrante IV")

# Condición de ubicación en el Orígen
elif x == 0 and y == 0:
    print("El punto (", x, ",", y, ") se encuentra en el Origen")

# Condición de ubicación en el Eje de las X
elif y == 0 and x != 0:
    print("El punto (", x, ",", y, ") se encuentra en el Eje de las X")

# Condición de ubicación en el Eje de las Y
elif x == 0 and y != 0:
    print("El punto (", x, ",", y, ") se encuentra en el Eje de las Y")

 