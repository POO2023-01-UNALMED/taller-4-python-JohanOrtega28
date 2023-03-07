class Asignatura:

    def __init__(self, nombre, salon="remoto"):
        self._nomnre = nombre
        self._salon = salon

    def __str__(self):
        return self._nombre + " " + self._salon