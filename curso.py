class Curso:
    total_cursos = 0  # Contador de instancias

    def __init__(self, nombre: str, codigo: str, descripcion: str):
        self.nombre = nombre
        self.codigo = codigo
        self.descripcion = descripcion
        Curso.total_cursos += 1  # Aumenta el contador cada vez que se crea un curso
    
    def mostrar_detalles(self):
        print('mostrar_detalles()')

    def actualizar_descripcion(self, nueva_descripcion: str):
        print('método actualizar_desc()')

    def __str__(self):
        return 'Método str'
    
    def __repr__(self):
        return 'Método repr'

    @classmethod
    def desde_tupla(cls, tupla):
        print('método de clase desde_tupla()')

    @staticmethod
    def es_curso_abierto():
        return bool()