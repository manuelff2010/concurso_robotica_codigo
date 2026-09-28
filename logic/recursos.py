class Recursos:
    def __init__(self, recursos):
        self._valores = recursos

    def obtener(self, nombre):
        return self._valores[nombre]

    def modificar(self, nombre, cambio):
        self._valores[nombre] = max(0, self._valores[nombre] + cambio) 
        return self._valores[nombre]

    def todos(self):
        return dict(self._valores) 

    def verificion(self):
        Recursos = [recurso for recurso, valor in self._valores.items() if valor == 0]
        if len(Recursos) != 0:
           return Recursos 
        return False
        