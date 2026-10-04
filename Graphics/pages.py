import dearpygui.dearpygui as dpg
import widgets as wd

class login_page:
    def __init__(self, dimensiones, dimensiones_ventana):
        self.ancho = dimensiones[0]
        self.alto = dimensiones[1]
        self.ancho_ventana = dimensiones_ventana[0]
        self.alto_ventana = dimensiones_ventana[1]
        self.texto = wd.Titulos("Acceso", "titulo")
    def centrar(self):
        self.ancho_ventana = dpg.get_viewport_client_width()
        x = (self.ancho_ventana - self.ancho) / 2
        y = (self.alto_ventana - self.alto) / 2
        dpg.set_item_pos("user", [x+10,y])
        dpg.set_item_pos("password", [x+10, y+30])
        dpg.set_item_pos("ingreso", [x+30, y+60])
        dpg.set_item_pos("registro", [x+30, y+90])
        self.texto.centrar(y-20, self.ancho_ventana)
    def build(self):
        self.texto.build()
        dpg.add_spacer(width=(self.ancho_ventana - self.ancho) / 2)
        dpg.add_input_text(tag="user", hint="Nombre de Usuario", width= self.ancho)
        dpg.add_input_text(tag="password", hint="Contraseña", width=self.ancho)
        dpg.add_button(tag="ingreso", label="Ingresar", width=self.ancho - 40, callback= self.get_dates)
        dpg.add_button(tag="registro", label="Registrarse", width=self.ancho - 40, callback= self.get_dates)
        self.centrar()
    
    def get_dates(self):
        print(dpg.get_value("user"))
        print(dpg.get_value("password"))
        return (dpg.get_value("user"), dpg.get_value("password"))
    
class user_page:
    def __init__(self, dimensiones, dimensiones_ventana):
        self.ancho = dimensiones[0]
        self.alto = dimensiones[1]
        self.ancho_ventana = dimensiones_ventana[0]
        self.alto_ventana = dimensiones_ventana[1]
        self.texto = wd.Titulos("Usuario", "titulo")
    def build(self):
        self.texto.build()
        self.boton_ancho = 450
        self.boton_alto = 40
        dpg.add_button(tag="nueva_mision", label="Nueva mision", width=  self.boton_ancho, height=self.boton_alto)
        dpg.add_button(tag="misiones_activas", label="Misiones activas", width=  self.boton_ancho, height=self.boton_alto)
        dpg.add_button(tag="top_globales", label="Top globales", width=  self.boton_ancho, height=self.boton_alto)
        dpg.add_button(tag="config", label="Config", width=  self.boton_ancho, height=self.boton_alto)
        dpg.add_button(tag="cerrar_sesion", label="Cerrar sesion", width=  self.boton_ancho, height=self.boton_alto)
        self.centrar()
        dpg.bind_item_theme("nueva_mision", "tema_botones_redondos")
        dpg.bind_item_theme("misiones_activas", "tema_botones_redondos")
        dpg.bind_item_theme("top_globales", "tema_botones_redondos")
        dpg.bind_item_theme("config", "tema_botones_redondos")
        dpg.bind_item_theme("cerrar_sesion", "tema_botones_redondos")
    def centrar(self):
        self.ancho_ventana = dpg.get_viewport_client_width()
        x = (self.ancho_ventana - self.boton_ancho ) / 2
        self.texto.centrar(20, self.ancho_ventana)
        base_y = 100
        base_spacing = 80
        dpg.set_item_pos(item = "nueva_mision", pos=[x, base_y])
        dpg.set_item_pos(item = "misiones_activas", pos=[x, base_y + base_spacing])
        dpg.set_item_pos(item = "top_globales", pos=[x, base_y + 2 * base_spacing])
        dpg.set_item_pos(item = "config", pos=[x, base_y + 3 * base_spacing])
        dpg.set_item_pos(item = "cerrar_sesion", pos=[x, base_y + 4 * base_spacing])

class juego_page:
    def __init__(self, dimensiones, dimensiones_ventana):
        self.ancho = dimensiones[0]
        self.alto = dimensiones[1]
        self.ancho_ventana = dimensiones_ventana[0]
        self.alto_ventana = dimensiones_ventana[1]
        self.texto = wd.Titulos("Panel de Mision", "titulo")
    def build(self):
        self.texto.build()
        dpg.add_separator()
        dpg.add_button(tag="volver", label="X", width= 30, height= 30)
        dpg.add_text("Mision: ", tag="mision_text", color=(255, 0, 90, 255))
        dpg.add_spacer(height=60)
        with dpg.tab_bar():        
        
            # --- PESTAÑA 1 ---
            with dpg.tab(label="Menu"):
                with dpg.group(horizontal=True):
                    dpg.add_button(label="+ AGREGAR")
                    dpg.add_button(label="- ELIMINAR")
                    dpg.add_button(label="EJECUTAR SIMULACIÓN")
                dpg.add_spacer(height=8)

    
            # --- PESTAÑA 2 ---
            with dpg.tab(label="Recursos"):
                with dpg.group(horizontal=True):
                    dpg.add_button(label="+ AGREGAR")
                    dpg.add_button(label="- ELIMINAR")
                    dpg.add_button(label="EJECUTAR SIMULACIÓN")
                dpg.add_spacer(height=8)
                # Segunda tabla con tag único (Evita que el tab se quede "vacío" o use el mismo tag)
                with dpg.table(tag="tabla_recursos", header_row=True,
                                borders_innerH=True, borders_outerH=True,
                                borders_innerV=True, borders_outerV=True,
                                row_background=True):
                    dpg.add_table_column(label="Componente")
                    dpg.add_table_column(label="Stock")
                    dpg.add_table_column(label="Ubicación")
    
            # --- PESTAÑA 3 ---
            with dpg.tab(label="Historial"):
                with dpg.group(horizontal=True):
                    dpg.add_button(label="+ AGREGAR")
                    dpg.add_button(label="- ELIMINAR")
                    dpg.add_button(label="EJECUTAR SIMULACIÓN")
                dpg.add_spacer(height=8)
                # Tercera tabla con tag único
                with dpg.table(tag="tabla_historial", header_row=True,
                                borders_innerH=True, borders_outerH=True,
                                borders_innerV=True, borders_outerV=True,
                                row_background=True):
                    dpg.add_table_column(label="Fecha/Hora")
                    dpg.add_table_column(label="Acción")
                    dpg.add_table_column(label="Usuario")
                
        self.centrar()
    def centrar(self):
        self.ancho_ventana = dpg.get_viewport_client_width()
        x = (self.ancho_ventana - 100 ) / 2
        self.texto.centrar(10, self.ancho_ventana)
        dpg.set_item_pos(item = "mision_text", pos=[50, 25])
        dpg.set_item_pos(item = "volver", pos=[10, 20])