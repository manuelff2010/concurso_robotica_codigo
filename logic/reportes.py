import json
import os

class Json_manager:
    def __init__(self, route):
        self.route = route
        self.file = None
    def leer_linea_especifica(self, numero_linea):
        try:
            with open(self.route, "r", encoding="utf-8") as archivo:
                lineas = archivo.readlines()
                if 1 <= numero_linea <= len(lineas):
                    return json.loads(lineas[numero_linea - 1].strip())
                print(f"Error: Línea {numero_linea} fuera de rango (Total: {len(lineas)}).")
                return None
 
        except FileNotFoundError:
            print("Error: El archivo no existe.")
            return None


    def modificar_linea_especifica(nombre_archivo, numero_linea, nueva_estructura):
        try:
            with open(nombre_archivo, "r", encoding="utf-8") as archivo:
                lineas = archivo.readlines()

            if 1 <= numero_linea <= len(lineas):
                nueva_linea_json = json.dumps(nueva_estructura, ensure_ascii=False) + "\n"
                lineas[numero_linea - 1] = nueva_linea_json

                with open(nombre_archivo, "w", encoding="utf-8") as archivo:
                    archivo.writelines(lineas)
            else:
                print(f"Error: Línea {numero_linea} fuera de rango.")
        except FileNotFoundError:
            print("Error: El archivo no existe.")

class Txt_manager:

    def __init__(self, route):
        self.route = route
        self.file = None
    
    def _open(self, mode='r'):
        if self.file is None:
            try:
                self.file = open(self.route, mode, encoding='utf-8')
                return True
            except FileNotFoundError:
                with open(self.route, 'w', encoding='utf-8') as f:
                    f.write("")
                self.file = open(self.route, mode, encoding='utf-8')
                return True
        return False

    def _close(self):
        if self.file != None:
            self.file.close()
            self.file = None
            return True
        return False

    def add(self, text):
        if self._open("a"):
            self.file.write(text + "\n")
            self._close()
            return True
        return False

    def add_list(self, lines_list):
        if self._open("a"):
            lines_with_newlines = ["- "+ line + f"\n" for line in lines_list]
            self.file.writelines(lines_with_newlines)
            self._close()
    
    def write_list(self, lines_list):
        if self._open("w"):
            lines_with_newlines = [line + f"\n\n" for line in lines_list]
            self.file.writelines(lines_with_newlines)
            self._close()
            return True
        return False

    def read(self):
        if self._open("r"):
            data = self.file.readlines()
            self._close()
            return data
        return False

class datas_saver():
    def guardar_partida(self, operadores_actuales, ruta_archivo="partida_save.json"):
        try:
            datos = [operador.to_dict() for operador in operadores_actuales]

            with open(ruta_archivo, "w", encoding="utf-8") as f:
                json.dump(datos, f, indent=4, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error al guardar la partida: {e}")
            return False


    def cargar_partida(self, clase, ruta_archivo="partida_save.json"):
        try:
            with open(ruta_archivo, "r", encoding="utf-8") as f:
                datos_lista = json.load(f)

            operadores_reconstruidos = [clase.from_dict(datos) for datos in datos_lista]
            return operadores_reconstruidos
            
        except FileNotFoundError:
            return []
        except Exception as e:
            return []

class report():
    def __init__(self, name: str, historial: list[str], estadisticas: str):
        self.historial = historial
        self.name = name 
        self.estadisticas = estadisticas
        os.makedirs("./reportes", exist_ok=True)
        self.manager = Txt_manager(f"./reportes/{name}_report.txt")

    def write(self, name):
        self.manager.add(f"reporte {name} sobre la mision: {self.name} \n")
        self.manager.add(self.estadisticas)
        self.manager.add_list(self.historial)