import dearpygui.dearpygui as dpg
import widgets as wid
import pages as pg



                ##dpg.render_dearpygui_frame()
class App:
    def __init__(self, ancho, alto, nombre):
        self.ancho = ancho
        self.alto = alto 
        self.nombre = nombre

    def build(self):
        self.login = pg.login_page([200,50], [self.ancho, self.alto])
        with dpg.window(tag="Manuex"):
            self.login.build()
    def ejecutar(self):
        dpg.create_context()
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