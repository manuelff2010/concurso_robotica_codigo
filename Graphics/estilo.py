import dearpygui.dearpygui as dpg
def cargar():
    with dpg.theme() as tema_cyberpunk:
            with dpg.theme_component(dpg.mvAll):
                dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (10, 10, 14, 255))
                dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (14, 14, 20, 255))
                dpg.add_theme_color(dpg.mvThemeCol_Text, (0, 255, 200, 255))          # cyan neón
                dpg.add_theme_color(dpg.mvThemeCol_Button, (30, 10, 40, 255))
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (255, 0, 90, 200))  # magenta al pasar mouse
                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (255, 0, 90, 255))
                dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (20, 20, 28, 255))        # fondo de inputs/celdas
                dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, (35, 35, 48, 255))
                dpg.add_theme_color(dpg.mvThemeCol_Tab, (20, 10, 30, 255))
                dpg.add_theme_color(dpg.mvThemeCol_TabActive, (255, 0, 90, 180))
                dpg.add_theme_color(dpg.mvThemeCol_TabHovered, (255, 0, 90, 120))
                dpg.add_theme_color(dpg.mvThemeCol_Border, (0, 255, 200, 100))
                dpg.add_theme_color(dpg.mvThemeCol_TableHeaderBg, (30, 10, 40, 255))
                dpg.add_theme_color(dpg.mvThemeCol_TableBorderStrong, (0, 255, 200, 150))
                dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 2)   # esquinas casi rectas = look "terminal"
                dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 1)
    with dpg.theme(tag="tema_botones_redondos"):
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 30, category=dpg.mvThemeCat_Core)
    return tema_cyberpunk