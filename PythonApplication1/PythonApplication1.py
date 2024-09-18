# Clase Libro
class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True  # El libro está disponible por defecto
    
    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' no está disponible.")

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print(f"El libro '{self.titulo}' ha sido devuelto.")
        else:
            print(f"El libro '{self.titulo}' ya está disponible.")

# Clase base Usuario
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = []
    
    def prestar_libro(self, libro):
        if libro.disponible:
            if len(self.libros_prestados) < self.limite_libros:
                libro.prestar()
                self.libros_prestados.append(libro)
            else:
                print(f"{self.nombre} ha alcanzado el límite de libros prestados.")
        else:
            print(f"El libro '{libro.titulo}' no está disponible para préstamo.")
    
    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            libro.devolver()
            self.libros_prestados.remove(libro)
        else:
            print(f"{self.nombre} no ha prestado el libro '{libro.titulo}'.")

# Clase Estudiante hereda de Usuario
class Estudiante(Usuario):
    limite_libros = 3  # Límite de libros que puede pedir un estudiante

# Clase Profesor hereda de Usuario
class Profesor(Usuario):
    limite_libros = 5  # Límite de libros que puede pedir un profesor

# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado a la biblioteca.")

    def eliminar_libro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)
            print(f"Libro '{libro.titulo}' eliminado de la biblioteca.")
        else:
            print(f"Libro '{libro.titulo}' no está en la biblioteca.")

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"Usuario '{usuario.nombre}' registrado en la biblioteca.")

    def prestar_libro_a_usuario(self, usuario, libro):
        usuario.prestar_libro(libro)

    def recibir_devolucion_de_usuario(self, usuario, libro):
        usuario.devolver_libro(libro)


# Ejemplo de uso:
# Crear biblioteca
biblioteca = Biblioteca()

# Crear algunos libros
libro1 = Libro("1984", "George Orwell", "12345")
libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", "67890")

# Agregar libros a la biblioteca
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Crear usuarios
estudiante = Estudiante("Juan Pérez")
profesor = Profesor("Dra. María García")

# Registrar usuarios en la biblioteca
biblioteca.registrar_usuario(estudiante)
biblioteca.registrar_usuario(profesor)

# Prestar libros
biblioteca.prestar_libro_a_usuario(estudiante, libro1)  # Juan pide 1984
biblioteca.prestar_libro_a_usuario(profesor, libro2)    # Dra. María pide El Principito

# Devolver libros
biblioteca.recibir_devolucion_de_usuario(estudiante, libro1)  # Juan devuelve 1984

