import logic.logic_main
from Terminal_graphics import menu  
class Terminal_app():
    def __init__(self):
        self.game = True
        self.menus = menu.Menus()
        self.init_loop()
    def init_loop(self):
        while self.game:
            match self.menus.actual_menu:
                case "salir":
                    self.game = False
                case "init":
                    self.menus.init_menu()
                case "user":
                    self.menus.user_menu()
                case "config":
                    self.menus.config_menu()
                case "sesion": 
                    self.menus.sesion_menu()
                case "misiones_activas":
                    self.menus.misiones_activas_menu()
                case "nueva_mision":
                    self.menus.nueva_mision_menu()
                case "juego":
                    self.menus.juego_menu()
                case "recursos":
                    self.menus.recursos_menu()
                case "execute_simulation":
                    self.menus.execute_simulation_menu()
                case "historial":
                    self.menus.historial_menu()

Terminal_app()