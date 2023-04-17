class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre  # Atributo nombre
        self.nota = nota  # Atributo nota

    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Nota:", self.nota)

    def resultado(self):
        if self.nota >= 6.5:
            print("El alumno", self.nombre, "ha aprobado.")
        else:
            print("El alumno", self.nombre, "ha suspendido.")

# Creamos un objeto de la clase Alumno y lo asignamos a la variable mi_alumno
mi_alumno = Alumno("Juan", 6)

# Imprimimos los atributos del objeto mi_alumno
mi_alumno.imprimir()

# Mostramos el resultado de la nota del objeto mi_alumno
mi_alumno.resultado()

# Creamos un objeto de la clase Alumno y lo asignamos a la variable mi_alumno
mi_alumno = Alumno("Cristian", 8)

# Imprimimos los atributos del objeto mi_alumno
mi_alumno.imprimir()

# Mostramos el resultado de la nota del objeto mi_alumno
mi_alumno.resultado()
