import dearpygui.dearpygui as dpg
import widgets as wid
import estilo
import pages_control as pgc
                ##dpg.render_dearpygui_frame()
class App:
    def __init__(self, ancho, alto, nombre):
        self.game = True
        self.ancho = ancho
        self.alto = alto 
        self.nombre = nombre
        self.pages = pgc.pages_manager(ancho, alto)
        self.pantallas = {
            "salir": lambda: setattr(self, "game", False),
            "init" : self.pages.init_menu,
            "user": self.pages.user_menu,
            "config": self.pages.config_menu,
            "sesion": self.pages.sesion_menu,
            "misiones_activas": self.pages.misiones_activas_menu,
            "nueva_mision": self.pages.nueva_mision_menu,
            "juego": self.pages.juego_menu,
            "recursos": self.pages.recursos_menu,
            "execute_simulation": self.pages.execute_simulation_menu,
            "historial": self.pages.historial_menu,
            "estadisticas": self.pages.estadisticas_menu,
            "finalizar_mision": self.pages.finalizar_mision_menu,
            "top_globales": self.pages.top_globales_menu
        }

    def build(self):
        self.login = pg.user_page([200,50], [self.ancho, self.alto])
        with dpg.window(tag="Manuex"):
            self.login.build()
    
    def ejecutar(self):
        dpg.create_context()
        dpg.bind_theme(estilo.cargar())
        dpg.create_viewport(title= self.nombre, width= self.alto, height= self.ancho)
        dpg.setup_dearpygui()
        dpg.show_viewport()
        self.build()
        dpg.set_primary_window("Manuex", True)
        dpg.set_viewport_resize_callback(self.redimensionar)
        dpg.start_dearpygui()
        dpg.destroy_context()

    def redimensionar(self):
        print("tung")
        self.login.centrar()

App(750, 600, "tung").ejecutar()