import dearpygui.dearpygui as dpg
import widgets as wd

class login_page:
    def __init__(self, dimensiones, dimensiones_ventana):
        self.ancho = dimensiones[0]
        self.alto = dimensiones[1]
        self.ancho_ventana = dimensiones_ventana[0]
        self.alto_ventana = dimensiones_ventana[1]
        self.texto = wd.Titulos("Ingreso", "titulo")
    def centrar(self):
        self.ancho_ventana = dpg.get_viewport_client_width()
        x = (self.ancho_ventana - self.ancho) / 2
        y = (self.alto_ventana - self.alto) / 2
        dpg.set_item_pos("user", [x,y])
        dpg.set_item_pos("password", [x, y+30])
        dpg.set_item_pos("ingreso", [x+30, y+60])
        self.texto.centrar(y-20, self.ancho_ventana)
    def build(self):
        self.texto.build()
        dpg.add_spacer(width=(self.ancho_ventana - self.ancho) / 2)
        dpg.add_input_text(tag="user", hint="Nombre de Usuario", width= self.ancho)
        dpg.add_input_text(tag="password", hint="Contraseña", width=self.ancho)
        dpg.add_button(tag="ingreso", label="tung", width=self.ancho - 40, callback= self.get_dates)
        self.centrar()
    def get_dates(self):
        print(dpg.get_value("user"))
        print(dpg.get_value("password"))
        return (dpg.get_value("user"), dpg.get_value("password"))
    
