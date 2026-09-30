from ast import List
import random as rd
from logic import usuarios as us
from logic import eventos as ev
from logic import misions as ms
class logic_app:
    def __init__(self):
        self.dificultad = 1
        self._sesion_iniciada = False
        self._users: us.Operador = []
        self.eventos: List[ev.Event] = []
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
                    self.active_user.sesion_iniciada = True
                    return
        self._sesion_iniciada = False
        self.active_user.sesion_iniciada = False
    def registro(self, name, password):
        for i in self._users:
            if i.name == name:
                return "usuario ya registrado"
        new_user = us.Operador(name, password)
        self._users.append(new_user)
        self.active_user = new_user
        self._sesion_iniciada = True
        self.active_user.sesion_iniciada = True

    """
    def get_misions(self):
        if self.sesion_iniciada:
            return [f"{mision.nombre}: {mision.type}" for mision in self.active_user.misiones]
    
    def get_preset_misions(self):
        return [mision["nombre"] for mision in ms.misiones_predefinidas]
    
    def append_mision(self, preset: int, name: str = None):
        if self.sesion_iniciada:
            mision_data = ms.misiones_predefinidas[preset-1]
            mision = ms.Mision(name, mision_data["descripcion"], mision_data["nombre"])
            mision.sources_init(mision_data["recursos"])
            self.active_user.misiones.append(mision)
    """
    def set_mision(self, index: int): 
        self.active_mision = self.active_user.misiones[index]
        self.active_mision.historial.append(f"mision {self.active_mision.nombre} abierta por {self.active_user.name}")
    
    def generate_event(self):
        longitud = len(ev.eventos)
        for i in range(self.dificultad):
            random_index = rd.randint(0, longitud - 1 + self.case_with_no_event)
            if not random_index >= longitud:
                evento = ev.eventos[random_index]
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
            self.active_mision.historial.append(f"evento {evento.name} : {evento.descripcion}")
            self.active_mision.historial.append(f"{self.active_user.name} ha seleccionado la opcion \"{option.title}\", correcta: {option.is_correct}")
            self.active_mision.historial.append(f"recursos: {self.active_mision.recursos.estados()}")
            self.active_mision.historial.append(f"estado de la mision: {self.active_mision.estado}")
  
    def execute_simulation(self):
        if self.active_mision.estado == "FINALIZADA" or self.active_mision.estado == "AGOTADO":
            return "partida finalizada"
            #final mision
        if len(self.eventos) > 0:
            return "aun hay eventos por responder"
        if self.active_mision.turno == 20:
            self.active_mision.estado = "FINALIZADA"
            return "partida finalizada"
        self.generate_event()
        self.active_mision.sources_turno()

        self.active_mision.turno += 1

    def actualizar_estado(self):
        if self.active_mision.estado != "FINALIZADA":
            self.active_mision.estado = self.active_mision.recursos.estado_general()

    def estadisticas_mision(self):
        mision = self.active_mision
        mision.puntuacion
        mision.type
        mision.nombre
        mision.descripcion
        mision.turno
        mision.eventos_procesados
        mision.eventos_mal_seleccionado
        eventos_bien = mision.eventos_procesados - mision.eventos_mal_seleccionado
        return {
                    "Eventos procesados": mision.eventos_procesados,
                    "Decisiones correctas": eventos_bien,
                    "Decisiones incorrectas": mision.eventos_mal_seleccionado,
                    "Energia restante": mision.recursos.obtener("energia"),
                    "Agua restante": mision.recursos.obtener("agua"),
                    "Alimento restante": mision.recursos.obtener("alimento"),
                    "Comunicaciones restantes": mision.recursos.obtener("comunicaciones"),
                    "Oxigeno restante": mision.recursos.obtener("oxigeno"),
                    "Aceptacion restante": mision.recursos.obtener("aceptacion"),
                    "Puntuacion final": mision.puntuacion,
                    "Indice de eficienccia": round((eventos_bien / mision.eventos_procesados) * 100, 2) if mision.eventos_procesados > 0 else 0,
                    "Estado final": mision.estado #repaso
                }