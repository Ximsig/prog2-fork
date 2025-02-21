class Curso:
    total_cursos = 0  # Contador de instancias

    def __init__(self, nombre: str, codigo: str, descripcion: str):
        self.nombre = nombre
        self.codigo = codigo
        self.descripcion = descripcion
        Curso.total_cursos += 1  # Aumenta el contador cada vez que se crea un curso
    
    def mostrar_detalles(self):
        pass

    def actualizar_descripcion(self, nueva_descripcion: str):
        pass

    def __str__(self):
        return 'Método str'
    
    def __repr__(self):
        pass

    @classmethod
    def desde_tupla(cls, tupla):
        pass