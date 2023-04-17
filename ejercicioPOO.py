# Definimos la clase Vehiculo
class Vehiculo:
    # El constructor de la clase recibe los atributos color, ruedas y puertas
    def __init__(self, color, ruedas, puertas):
        self.color = color  # Atributo color
        self.ruedas = ruedas  # Atributo ruedas
        self.puertas = puertas  # Atributo puertas

# Definimos la clase Coche, que hereda de la clase Vehiculo
class Coche(Vehiculo):
    # El constructor de la clase recibe los atributos color, ruedas, puertas, velocidad y cilindrada
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)  # Llamamos al constructor de la clase padre
        self.velocidad = velocidad  # Atributo velocidad
        self.cilindrada = cilindrada  # Atributo cilindrada

# Creamos un objeto de la clase Coche y lo asignamos a la variable mi_coche
mi_coche = Coche("Rojo", 4, 5, 120, 2000)

# Mostramos el objeto por consola utilizando la función print()
print("Color:", mi_coche.color)  # Accedemos al atributo color del objeto mi_coche
print("Ruedas:", mi_coche.ruedas)  # Accedemos al atributo ruedas del objeto mi_coche
print("Puertas:", mi_coche.puertas)  # Accedemos al atributo puertas del objeto mi_coche
print("Velocidad:", mi_coche.velocidad)  # Accedemos al atributo velocidad del objeto mi_coche
print("Cilindrada:", mi_coche.cilindrada)  # Accedemos al atributo cilindrada del objeto mi_coche
