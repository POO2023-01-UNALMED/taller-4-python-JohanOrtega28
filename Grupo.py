
from classroom.asignatura import Asignatura
from classroom.asignatura import Asignatura


class Grupo:

    grado = None
    
    def __init__(self, grupo="grupo predeterminante", asignaturas=NOne, estudiantes=None, grado = "Grado 12"):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self._listadoAlumnos = estudiantes
        self.grado = grado

    def listadoAsignaturas(self, **kwargs):
        if self.asignaturas == None:
            self._asignaturas = []
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if self._listadoAlumnos == None:
            self._listadoAlumnos = []
        if lista ==None:
            lista[]
        lista.append(alumno)
        self._listadoAlumnos = self._listadoAlumnos + lista

    @classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    def __str__(self) -> str:
        return "Grupo de estudiantes: " + self._grupo