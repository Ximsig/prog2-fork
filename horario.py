class Horario:
    total_horarios = 0  # Contador de instancias

    def __init__(self, curso, dia, hora_inicio, hora_fin):
        self.curso = curso
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        Horario.total_horarios += 1  # Aumenta el contador cada vez que se crea un horario

    def mostrar_horario():
        pass
    
    def modificar_horario():
        pass
    
    def __str__():
        pass

    def __repr__():
        pass

    def desde_tupla(cls, tupla):
        pass

    def es_horario_valido():
        pass
    