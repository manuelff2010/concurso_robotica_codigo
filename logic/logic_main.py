from ast import List
import random as rd
from logic import usuarios as us
from logic import eventos

class logic_app:
    def __init__(self):
        self.dificultad = 1
        self._sesion_iniciada = False
        self._users: us.Operador = []
        self.eventos: List[eventos.Event] = []
        self.active_user: us.Operador = None
        self.active_mision = None
        self.case_with_no_event = 1
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
                    return
        self._sesion_iniciada = False

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
        if self.sesion_iniciada:
            mision_data = us.misiones_predefinidas[preset-1]
            mision = us.mision(name, mision_data["descripcion"], mision_data["nombre"])
            mision.sources_init(mision_data["recursos"])
            self.active_user.misiones.append(mision)
    def set_mision(self, index: int):
        self.active_mision = self.active_user.misiones[index]

    def generate_event(self):
        longitud = len(eventos.eventos)
        for i in range(self.dificultad):
            random_index = rd.randint(0, longitud - 1 + self.case_with_no_event)
            if not random_index >= longitud:
                evento = eventos.eventos[random_index]
                self.eventos.append(evento)
    
    def get_event(self, index):
        if len(self.eventos) > 0:
            return self.eventos[index]
        else:
            return None
    
    def process_event(self, option, index):
        evento = self.eventos[index]
        if option in evento.opciones:
            cambiar_recurso = self.active_mision.recursos.modificar
        
            for recurso, valor in evento.activate(option).items():
                if recurso != "puntos":
                    cambiar_recurso(recurso, valor)
            self.active_mision.modify_puntuacion(option.consecuences["puntos"])
            if option.is_correct == False:
                self.active_mision.eventos_mal_seleccionado += 1
            self.active_mision.eventos_procesados += 1
            self.actualizar_estado()

    def execute_simulation(self):
        if self.active_mision.estado == "FINALIZADA" or self.active_mision.estado == "AGOTADO":
            return "partida finalizada"
        if len(self.eventos) > 0:
            return "aun hay eventos por responder"
        if self.active_mision.turno == 20:
            self.active_mision.estado = "FINALIZADA"
            return "partida finalizada"
        self.generate_event()
        if self.active_mision.estado == "AGOTADO":
            pass #generar reporte
        self.active_mision.sources_turno()

        self.active_mision.turno += 1
    def actualizar_estado(self):
        if self.active_mision.estado != "FINALIZADA":
            self.active_mision.estado = self.active_mision.recursos.estado_general()