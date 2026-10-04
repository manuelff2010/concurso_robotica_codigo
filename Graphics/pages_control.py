import pages as pg

class pages_manager():
    def __init__(self, ancho, alto):
        self.actual_menu = "init"
        self.ancho = ancho
        self.alto = alto
        self.pantallas = {
            "salir": lambda: setattr(self, "game", False),
            "init" : self.init_menu,
            "user": self.user_menu,
            "config": self.config_menu,
            "sesion": self.sesion_menu,
            "misiones_activas": self.misiones_activas_menu,
            "nueva_mision": self.nueva_mision_menu,
            "juego": self.juego_menu,
            "recursos": self.recursos_menu,
            "execute_simulation": self.execute_simulation_menu,
            "historial": self.historial_menu,
            "estadisticas": self.estadisticas_menu,
            "finalizar_mision": self.finalizar_mision_menu,
            "top_globales": self.top_globales_menu
        }
    def init_menu(self):
        self.init = pg.init_page([200,50], [self.ancho, self.alto])
        self.init.execute()