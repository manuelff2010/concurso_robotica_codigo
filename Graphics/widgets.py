

import dearpygui.dearpygui as dpg

class Titulos():
    def __init__(self, texto, tag, pos = [100,100]):
        self.texto = texto
        self.x = pos[0]
        self.y = pos[1]
        self.tag = tag
        dpg.render_dearpygui_frame()
        self.ancho = dpg.get_text_size(self.texto)[0]
    def build(self):
        dpg.add_text(self.texto, tag= self.tag, pos= [self.x, self.y])
    def centrar(self, y, ancho_ventana):
        self.y = y
        self.x =  (ancho_ventana - self.ancho) / 2
        dpg.set_item_pos(self.tag, pos = [self.x, self.y])