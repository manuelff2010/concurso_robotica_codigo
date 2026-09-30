from struct import calcsize

from logic import logic_main
class Menu_displayer:
    
    ENTRAR_PANTALLA_ALT = "\033[?1049h"
    SALIR_PANTALLA_ALT = "\033[?1049l"
    LIMPIAR_PANTALLA = "\033[H\033[2J"
    AZUL = "\033[34m"
    VERDE = "\033[32m"
    AMARILLO = "\033[33m"
    RESET = "\033[0m"
    
    def __init__(self, title: str, options: list[str]):
        self.title = f"{self.VERDE}{title}{self.RESET}"
        self.menu_options = options

    def Menu_activate(self, numbered: bool = True, rel_num: bool = True, min_characters: int = 0):
        run = True
        print(self.ENTRAR_PANTALLA_ALT + self.LIMPIAR_PANTALLA, end="")
        while run:
            print(self.LIMPIAR_PANTALLA)
            print(self.title)
            print("-------------------")
            for i in range(len(self.menu_options)):
                if numbered:
                    print(f"{self.AMARILLO}{i+1}. {self.menu_options[i]}{self.RESET}")
                else:
                    print(f"{self.AMARILLO}- {self.menu_options[i]}{self.RESET}")
            
            entrada = input(f"{self.AZUL}$: {self.RESET}")
            if rel_num:
                if self.entry_verication(entrada) != None: 
                    run = False
                    print(self.LIMPIAR_PANTALLA)
                    print(self.SALIR_PANTALLA_ALT)
                    return self.entry_verication(entrada)
            
            if len(entrada) >= min_characters and rel_num == False:
                print(self.LIMPIAR_PANTALLA)
                print(self.SALIR_PANTALLA_ALT)
                return entrada
    
    def entry_verication(self, entry: str):
            try:
                int(entry)
                if int(entry) <= 0 or int(entry) > len(self.menu_options):
                    return print(f"{self.AMARILLO}Entrada invalida{self.RESET}")
                return int(entry)
            except ValueError:
                print(f"{self.AMARILLO}Entrada invalida{self.RESET}")


class Menus():
    def __init__(self):
        self.logic = logic_main.logic_app()
        self.actual_menu = "init"

    def state_updater(self, state):
        if not isinstance(state, (tuple, list)):
            state = [state]

        for accion in state:
            if isinstance(accion, str):
                self.variable_estado = accion

            elif callable(accion):
                accion() 
    
    def state_updater(self, states: list[str | callable], rel: int, volver: str = None):
        if volver != None and rel == len(states):
            self.actual_menu = volver
        if rel < len(states):
            if not isinstance(states, (tuple, list)):
                states = [states]
            if isinstance(states[rel], str):
                    self.actual_menu = states[rel-1]
            if callable(states[rel]):
                    states[rel]()
        return False
    
    def init_menu(self):
        rel = Menu_displayer("Bienvenido", ["iniciar sesion","registrarse","salir"]).Menu_activate()
        match(rel):
            case 1:
                self.logic.sesion_iniciada = self.sesion_menu()
                if self.logic.sesion_iniciada:
                    self.actual_menu = "user"
                else:
                    self.actual_menu = "init"
            case 2:
                nombre, password = self.sesion_menu()
                self.logic.registro(nombre, password)
                if self.logic.sesion_iniciada:
                    self.actual_menu = "user"
                else:
                    Menu_displayer("Error al registrar usuario", ["Presiona [ENTER] para volver"]).Menu_activate(False, False)
                    self.actual_menu = "init"
            case 3:
                self.actual_menu = "salir"
    
            case _:
                self.actual_menu = "init"

    def user_menu(self):
        rel = Menu_displayer(f"Bienvenido {self.logic.active_user.name}", ["nueva mision","misiones activas","config","cerrar sesion"]).Menu_activate()
        match(rel):
            case 1:
                self.actual_menu = "nueva_mision"
            case 2:
                self.actual_menu = "misiones_activas"
            case 3:
                self.actual_menu = "config"
            case 4:
                self.logic.cerrar_sesion()
                self.actual_menu = "init"
            case _:
                self.actual_menu = "user"
    
    def config_menu(self):
        rel = Menu_displayer("configuracion", ["volver"]).Menu_activate()
        match rel:
            case 1:
                self.actual_menu = "user"

    def sesion_menu(self):
        nombre =  Menu_displayer(f"Pronto comenzara la mision ingresa tus datos \n (minimo 4 caracteres)", ["Nombre: "]).Menu_activate(False, False, 4)
        contraseña = Menu_displayer(f"Pronto comenzara la mision ingresa tus datos \n (minimo 4 caracteres)", ["contraseña: "]).Menu_activate(False, False, 4)
        return nombre, contraseña
    
    def misiones_activas_menu(self):
        misiones = self.logic.active_user.get_misions().copy()
        misiones.append("volver")
        rel = Menu_displayer("Misiones activas:", misiones).Menu_activate()
        if rel == len(misiones):
            self.actual_menu = "user"
        else:
            self.logic.set_mision(rel - 1)
            self.actual_menu = "juego"

    def nueva_mision_menu(self):
        options = self.logic.active_user.get_preset_misions().copy()
        options.append("volver")
        name =  Menu_displayer("Nueva mision", ["nombre"]).Menu_activate(False, False)
        type =  Menu_displayer("Selecciona el tipo de mision que quieres", options).Menu_activate()
        if type == len(options):
            self.actual_menu = "user"
            return
        self.logic.active_user.append_mision(type, name)
        self.logic.set_mision(-1)
        self.actual_menu = "juego"

    def juego_menu(self):
        rel = Menu_displayer(f"Mision: {self.logic.active_mision.nombre} \n- turno actual: {self.logic.active_mision.turno} | Estado: {self.logic.active_mision.estado}",
                       ["recursos","ejecutar simulacion","historial","estadicticas","volver"]).Menu_activate()
        self.state_updater(["recursos","execute_simulation","historial","estadisticas","misiones_activas"], rel, "misiones_activas")
 
    def finalizar_mision_menu(self):
        rel = Menu_displayer("la mision ha finalizado", ["recursos", "historial", "estadisticas", "generar reporte", "eliminar mision", "volver a misiones"]).Menu_activate()
        match rel:
            case 1:
                self.actual_menu = "recursos"
            case 2:
                self.actual_menu = "historial"
            case 3:
                self.actual_menu = "estadisticas"
            case 4:
                pass #generar reporte
            case 5:
                self.actual_menu = "misiones_activas"
            case 6:
                self.actual_menu = "misiones_activas"
    
    def recursos_menu(self):
        agua = self.logic.active_mision.recursos.obtener("agua")
        energia = self.logic.active_mision.recursos.obtener("energia")
        alimento = self.logic.active_mision.recursos.obtener("alimento")
        comunicaciones = self.logic.active_mision.recursos.obtener("comunicaciones")
        oxigeno = self.logic.active_mision.recursos.obtener("oxigeno")
        aceptacion = self.logic.active_mision.recursos.obtener("aceptacion")
        Menu_displayer("recursos: ", [f"Agua:           {agua} | estado: {self.logic.active_mision.recursos.estados()['agua']}",
                                      f"alimento:       {alimento} | estado: {self.logic.active_mision.recursos.estados()['alimento']}",
                                      f"energia:        {energia} | estado: {self.logic.active_mision.recursos.estados()['energia']}",
                                      f"comunicaciones: {comunicaciones} | estado: {self.logic.active_mision.recursos.estados()['comunicaciones']}",
                                      f"oxigeno:        {oxigeno} | estado: {self.logic.active_mision.recursos.estados()['oxigeno']}",
                                      f"aceptacion:     {aceptacion} | estado: {self.logic.active_mision.recursos.estados()['aceptacion']}",
                                      "Presiona [ENTER] para devolverte"]).Menu_activate(False, False)
        self.actual_menu = "juego"

    def execute_simulation_menu(self):
        self.logic.execute_simulation()
        Menu_displayer("Simulation ejecutada", ["Presiona [ENTER] para Seguir"]).Menu_activate(False, False)
        for indice, event in enumerate(self.logic.eventos):
            while True:
                rel = Menu_displayer(f"evento: {event.name} \n {event.descripcion}",[opcion.title for opcion in event.opciones]).Menu_activate()
                match rel:
                    case 1:
                        self.logic.process_event(event.opciones[0], indice)
                        break
                    case 2:
                        self.logic.process_event(event.opciones[1], indice)
                        break
        self.actual_menu = "juego"
        self.logic.eventos.clear()
        
    def historial_menu(self):
        historial = self.logic.active_mision.historial.copy()
        historial.append("Presiona [ENTER] para volver")
        rel = Menu_displayer("Historial menu", historial).Menu_activate(False, False)
        self.actual_menu = "juego"

    def estadisticas_menu(self):
        estadisticas = self.logic.estadisticas_mision()
        estadisticas_list = [f"{key}: {value}" for key, value in estadisticas.items()]
        estadisticas_list.append("Presiona [ENTER] para volver")
        rel = Menu_displayer("Estadisticas de la mision", estadisticas_list).Menu_activate(False, False)
        self.actual_menu = "juego"