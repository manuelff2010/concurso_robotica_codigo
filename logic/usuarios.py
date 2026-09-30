from logic import misions as ms
class Operador():
    
    def __init__(self, name: str, password: str):
        self.name = name
        self.__password = password
        self.misiones = []
        self.privilegios = "operador"
        self.sesion_iniciada = False
    
    @property
    def password(self):
        return "*******"

    @password.setter
    def password(self, new_password):
        if len(new_password > 7):
            self.__password = new_password
            print("Contraseña actualizada con éxito.")
        raise ValueError("La contraseña debe tener al menos 8 caracteres.")

    def verificate(self, password_chance):
        if password_chance == self.__password:
            return True
        return False

    def get_misions(self):
            if self.sesion_iniciada:
                return [f"{mision.nombre}: {mision.type}" for mision in self.misiones]
        
    def get_preset_misions(self):
        return [mision["nombre"] for mision in ms.misiones_predefinidas]
    
    def append_mision(self, preset: int, name: str = None):
        if self.sesion_iniciada:
            mision_data = ms.misiones_predefinidas[preset-1]
            mision = ms.Mision(name, mision_data["descripcion"], mision_data["nombre"])
            mision.sources_init(mision_data["recursos"])
            self.misiones.append(mision)
    
    