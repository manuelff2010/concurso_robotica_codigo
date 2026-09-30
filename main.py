import logic.logic_main
from Terminal_graphics import menu  

class Terminal_app():
    def __init__(self):
        self.game = True
        self.menus = menu.Menus()
        self.pantallas = {
            "salir": lambda: setattr(self, "game", False),
            "init" : self.menus.init_menu,
            "user": self.menus.user_menu,
            "config": self.menus.config_menu,
            "sesion": self.menus.sesion_menu,
            "misiones_activas": self.menus.misiones_activas_menu,
            "nueva_mision": self.menus.nueva_mision_menu,
            "juego": self.menus.juego_menu,
            "recursos": self.menus.recursos_menu,
            "execute_simulation": self.menus.execute_simulation_menu,
            "historial": self.menus.historial_menu,
            "estadisticas": self.menus.estadisticas_menu,
            "finalizar_mision": self.menus.finalizar_mision_menu
        }
        self.init_loop()
    def init_loop(self):
        while self.game:
            for i in self.pantallas.keys():
                if i == self.menus.actual_menu:
                    self.pantallas[i]()
                    break
                
Terminal_app()