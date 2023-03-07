
from classroom.asignatura import Asignatura
from classroom.asignatura import Asignatura


class Grupo:

    grado = None

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None, grado = "Grado 12"):
        self._grupo = grupo
        self._asignatruras = asignaturas
        self.listadoAlumnos = estudiantes
        self.grado = grado

    def listadoAsignaturas(self, **kwargs):
        if self._asignatruras == None:
            self._asignatruras = []
        for x in kwargs.values():
            self._asignatruras.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if self.listadoAlumnos == None:
            self.listadoAlumnos = []
        if lista == None:
            lista = []
        lista.append(alumno)
        self.listadoAlumnos = self.listadoAlumnos + lista

    @classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
    
    def __str__(self) -> str:
        return "Grupo de estudiantes: " + self._grupo