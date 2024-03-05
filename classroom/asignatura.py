class Asignatura:

    def __init__(self, nombre= None, salon= None):
        self._nombre = nombre
        if salon is None:
            self._salon = "remoto"
        else:
            self._salon = salon

    def salon(self):
        return self._salon
    def nombre(self):
        return self._nombre
    def __str__(self):
        return self._nombre + " " + self._salon
