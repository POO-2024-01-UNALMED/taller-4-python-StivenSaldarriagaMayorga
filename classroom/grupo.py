from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 6"

    def __init__(self, grupo=None, asignaturas=None, estudiantes=None):
        if grupo is None:
            self._grupo = "grupo predeterminado"
        else:    
            self._grupo = grupo
        if asignaturas is None:
            self._asignaturas = []
        else:
            self._asignaturas = asignaturas
        if estudiantes is None:
            self.listadoAlumnos = []
        else:
            self.listadoAlumnos = estudiantes

    
    
    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if lista is None:
            lista=[]
            lista.append(alumno)
            self.listadoAlumnos = self.listadoAlumnos + lista
        else:
            lista.append(alumno)
            self.listadoAlumnos = self.listadoAlumnos + lista

    def __str__(self):
        return "Grupo de estudiante: " + self._grupo




    @ classmethod
    def asignarNombre(cls, nombre=None):
            if nombre is None:
                cls.grado = "Grado 6"
            else:
                cls.grado = nombre



    # @ classmethod
    # def asignarNombre(cls, nombre="Grado 6"):
    #         cls.grado = nombre
        
    # @ classmethod
    # def asignarNombre(cls, nombre="Grado 4"):
    #         cls.grado = nombre