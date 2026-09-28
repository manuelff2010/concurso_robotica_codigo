import random as rd
from logic import usuarios as us
class logic_app:
    def __init__(self):
        self._sesion_iniciada = False
        self._users: us.Operador = []
        self.eventos = []
        self.active_user: us.Operador = None
        self.active_mision = None

    @property
    def sesion_iniciada(self):
        return self._sesion_iniciada

    def cerrar_sesion(self):
        self._sesion_iniciada = False
        self.active_user = None

    @sesion_iniciada.setter
    def sesion_iniciada(self, credenciales):
        user = credenciales[0]
        password = credenciales[1]
        for u in self._users:
            if u.name == user:
                if u.verificate(password):
                    self.active_user = u
                    self._sesion_iniciada = True
                else:
                    return "contraseña no valida"
        return "nombre de usuario no registrado"

    def registro(self, name, password):
        for i in self._users:
            if i.name == name:
                return "usuario ya registrado"
        new_user = us.Operador(name, password)
        self._users.append(new_user)
        self.active_user = new_user
        self._sesion_iniciada = True

    def get_misions(self):
        if self.sesion_iniciada:
            return [f"{mision.nombre}: {mision.type}" for mision in self.active_user.misiones]
    
    def get_preset_misions(self):
        return [mision["nombre"] for mision in us.misiones_predefinidas]
    
    def append_mision(self, preset: int, name: str = None):
        print(preset)
        if self.sesion_iniciada:
            mision_data = us.misiones_predefinidas[preset-1]
            mision = us.mision(name, mision_data["descripcion"], mision_data["nombre"])
            mision.sources_init(mision_data["recursos"])
            self.active_user.misiones.append(mision)
    def set_mision(self, index: int):
        self.active_mision = self.active_user.misiones[index]
        print(self.active_mision.nombre)
        print(self.active_mision.turno)


    def delete_mision(self, mision_name):
        for mision in self.active_user.misiones:
            if mision.name == mision_name:
                pass