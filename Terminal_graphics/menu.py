import logic.logic_main

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

    def Menu_activate(self, numbered: bool = True, rel_num: bool = True):
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
            try:
                entrada = input(f"{self.AZUL}$: {self.RESET}")
                if rel_num:
                    if self.entry_verication(entrada) != None: 
                        run = False
                        print(self.LIMPIAR_PANTALLA)
                        print(self.SALIR_PANTALLA_ALT)
                        return self.entry_verication(entrada)
                else:
                    print(self.LIMPIAR_PANTALLA)
                    print(self.SALIR_PANTALLA_ALT)
                    return entrada
            except:
                print("el valor debe ser un numero dentro de las opciones")
    def entry_verication(self, entry: str):
            try:
                int(entry)
                if int(entry) <= 0:
                    return None
                return int(entry)
            except:
                return None


class Menus():
    def __init__(self):
        self.logic = logic.logic_main.logic_app()
        self.actual_menu = "init"
    def init_menu(self):
        rel = Menu_displayer("Bienvenido", ["inicar sesion","registrarse","salir"]).Menu_activate()
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
        pass

    def sesion_menu(self):
        nombre =  Menu_displayer("Pronto comenzara la mision ingresa tus datos", ["Nombre: "]).Menu_activate(False, False)
        contraseña = Menu_displayer("Pronto comenzara la mision ingresa tus datos", ["contraseña: "]).Menu_activate(False, False)
        return nombre, contraseña
    
    def misiones_activas_menu(self):
        misiones = self.logic.get_misions().copy()
        misiones.append("volver")
        rel = Menu_displayer("Misiones activas:", misiones).Menu_activate()
        if rel >= len(misiones):
            self.actual_menu = "user"
        else:
            self.logic.set_mision(rel - 1)
            self.actual_menu = "juego"

    def nueva_mision_menu(self):
        options = self.logic.get_preset_misions().copy()
        options.append("volver")
        name =  Menu_displayer("Nueva mision", ["nombre"]).Menu_activate(False, False)
        type =  Menu_displayer("Selecciona el tipo de mision que quieres", options).Menu_activate()
        if type >= len(options):
            self.actual_menu = "user"
        self.logic.append_mision(type, name)
        self.logic.set_mision(-1)
        self.actual_menu = "juego"

    def juego_menu(self):
        rel = Menu_displayer(f"{self.logic.active_mision.nombre} \n -turno actual: {self.logic.active_mision.turno}",
                       ["recursos","ejecutar simulacion","historial","volver"]).Menu_activate()
        match rel:
            case 1:
                self.actual_menu = "recursos"
            case 2:
                self.actual_menu = "execute_simulation"
            case 3:
                self.actual_menu = "historial"
            case 4:
                self.actual_menu = "misiones_activas"

    def recursos_menu(self):
        agua = self.logic.active_mision.recursos.obtener("agua")
        energia = self.logic.active_mision.recursos.obtener("energia")
        alimento = self.logic.active_mision.recursos.obtener("alimento")
        comunicaciones = self.logic.active_mision.recursos.obtener("comunicaciones")
        oxigeno = self.logic.active_mision.recursos.obtener("oxigeno")
        aceptacion = self.logic.active_mision.recursos.obtener("aceptacion")
        Menu_displayer("recursos: ", [f"Agua: {agua}",f"alimento: {alimento}",f"energia: {energia}",f"comunicaciones: {comunicaciones}",
                                             f"oxigeno: {oxigeno}",f"aceptacion: {aceptacion}","Presiona [ENTER] para devovlerte"]).Menu_activate(False, False)
        self.actual_menu = "juego"
    def execute_simulation_menu(self):
        return Menu_displayer().Menu_activate("Simulation menu")
    
    def historial_menu(self):
        return Menu_displayer().Menu_activate("Historial menu")