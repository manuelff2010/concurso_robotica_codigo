from ast import List
import random as rd
from logic import usuarios as us
from logic import eventos as ev
from logic import reportes as rp
class logic_app:
    def __init__(self):
        self.data_saver = rp.datas_saver()
        self._sesion_iniciada = False
        self._users: us.Operador = self.data_saver.cargar_partida(us.Operador)
        self.eventos: List[ev.Event] = []
        self.active_user: us.Operador = None
        self.active_mision = None
        self.case_with_no_event = 1
        self.turnos_por_mision = 5    
        self.top_globales = []

    @property
    def sesion_iniciada(self):
        return self._sesion_iniciada

    def cerrar_sesion(self):
        self._sesion_iniciada = False
        self.active_user.sesion_iniciada = False
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

    def registro(self, name, password):
        for i in self._users:
            if i.name == name:
                return "usuario ya registrado"
        new_user = us.Operador(name, password)
        if len(self._users) == 0:
            new_user.privilegios = "admin"
        self._users.append(new_user)
        self.active_user = new_user
        self._sesion_iniciada = True
        self.active_user.sesion_iniciada = True
        self.data_saver.guardar_partida(self._users)

    def get_users(self):
        return [f"{user.name}: {user.privilegios}" for user in self._users]

    def delete_user(self, name):
        for i in self._users:
            if i.name == name:
                self._users.remove(i)
                self.data_saver.guardar_partida(self._users)
                return "usuario eliminado"
        return "usuario no encontrado"

    def modify_privilegios(self, name, privilegios):
        for i in self._users:
            if i.name == name:
                i.privilegios = privilegios
                self.data_saver.guardar_partida(self._users)
                return True
        return False
   
    def set_mision(self, index: int): 
        self.active_mision = self.active_user.misiones[index]
        self.active_mision.historial.append(f"mision {self.active_mision.nombre} abierta por {self.active_user.name}")
    
    def generate_event(self):
        longitud = len(ev.eventos)
        for i in range(self.active_mision.dificultad):
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
            self.data_saver.guardar_partida(self._users)
  
    def execute_simulation(self):
        if self.active_mision.partida_finalizada:
            return
        if len(self.eventos) > 0:
            self.data_saver.guardar_partida(self._users)
            return "aun hay eventos por responder"
        if self.active_mision.recursos.estado_general() == "AGOTADO" or self.active_mision.estado == "AGOTADO":
                    self.active_mision.estado = "FALLIDA"
                    self.active_mision.partida_finalizada = True
                    self.data_saver.guardar_partida(self._users)
                    self.active_mision.historial.append(f"mision {self.active_mision.nombre} finalizada")
                    return "partida finalizada"
        if self.active_mision.turno == self.turnos_por_mision:
            self.active_mision.estado = "COMPLETADA"
            self.active_mision.partida_finalizada = True
            self.data_saver.guardar_partida(self._users)
            self.active_mision.historial.append(f"mision {self.active_mision.nombre} finalizada")
            return "partida finalizada"
        self.generate_event()
        self.active_mision.sources_turno()
        self.active_mision.turno += 1
        self.active_mision.historial.append(f"recursos: \n{self.active_mision.recursos.historial_data()}")
        self.active_mision.historial.append(f"estado de la mision: {self.active_mision.estado}")

    def actualizar_estado(self):
        if not self.active_mision.partida_finalizada:
            self.active_mision.estado = self.active_mision.recursos.estado_general()

    def eliminar_mision(self):
        self.active_user.delete_mision(self.active_mision)
        self.active_mision = None
    
    def generar_reporte(self):
        estadisticas = "" 
        for categoria, valor in self.active_mision.estadisticas_mision().items():
            estadisticas += f"{categoria}: {valor}\n"
        if self.active_mision != None:
            rp.report(self.active_mision.nombre, self.active_mision.historial, estadisticas).write(self.active_user.name)

    def top_globales_update(self):
        ranking = []
        if len(self._users) > 0:
            for user in self._users:
                for mision in user.misiones:
                    ranking.append((user, mision.estadisticas_mision()["Puntuacion final"], mision))
        ranking.sort(key= lambda x : x[1], reverse=True)
        self.top_globales = ranking
        return
    
