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


    def verificate(self, password_chance):
        if password_chance == self.__password:
            return True
        return False

    def get_misions(self):
            if self.sesion_iniciada:
                return [f"{mision.nombre}: {mision.type}" for mision in self.misiones]
        
    def get_preset_misions(self):
        return [mision["nombre"] for mision in ms.misiones_predefinidas]
    
    def append_mision(self, preset: int, name: str = None, dificultad: int = 1):
        if self.sesion_iniciada:
            mision_data = ms.misiones_predefinidas[preset-1]
            if mision_data.get("aleatorio"):
                mision_data = {**mision_data, "recursos": ms.generar_recursos_aleatorios()}
            mision = ms.Mision(name, mision_data["descripcion"], mision_data["nombre"], dificultad)
            mision.sources_init(mision_data["recursos"])
            self.misiones.append(mision)

    def delete_mision(self, mision: ms.Mision):
        self.misiones.remove(mision)

    def to_dict(self):
            return {
                "name": self.name,
                "password": self.__password, 
                "privilegios": self.privilegios,
                "misiones": [m.to_dict() for m in self.misiones]
            }
    
    @classmethod
    def from_dict(cls, data):
        if not data: return None
        operador = cls(data["name"], data["password"])
        operador.privilegios = data["privilegios"]
        operador.misiones = [ms.Mision.from_dict(m_dict) for m_dict in data["misiones"]]
        return operador