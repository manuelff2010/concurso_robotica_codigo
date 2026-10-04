from logic import recursos
import random as rd

class Mision():
    
    def __init__(self, nombre: str, descripcion: str, type: str, dificultad: int = 1):
        self.nombre = nombre
        self.descripcion = descripcion
        self.type = type
        self.estado = "INICIALIZADO"
        self.puntuacion = 0
        self.turno = 0
        self.dificultad = dificultad
        self.partida_finalizada = False
        self.eventos_procesados = 0
        self.eventos_mal_seleccionado = 0
        self.historial = []
        self.recursos_iniciales = {}
        self.historial.append(f"mision {self.nombre} inicializada")
        self.historial.append(f"mision: {self.descripcion}")
    
    def sources_init(self, recursoso_iniciales: dict):
        self.recursos = recursos.Recursos(recursoso_iniciales)
        self.recursos_iniciales = recursoso_iniciales.copy()
        self.historial.append(f"recursos iniciales: \n")
        for nombre in self.recursos.estados().keys():
            self.historial.append(f"{nombre}: {self.recursos.obtener(nombre)}")

    def porcentaje(self, recurso):
        inicial = self.recursos_iniciales.get(recurso, 0)
        if inicial <= 0:
            return None
        return round((self.recursos.obtener(recurso) / inicial) * 100, 2)

    def estado_recurso(self, recurso):
        valor = self.recursos.obtener(recurso)
        porcentaje = self.porcentaje(recurso)
        if porcentaje is None:
            return str(valor)
        return f"{valor} ({porcentaje}%)"
    
    def modify_puntuacion(self,valor):
        self.historial.append(f"Se actualiza puntuacion de {self.puntuacion}, a {self.puntuacion + valor}")
        self.puntuacion += valor
    
    def sources_turno(self):
        recursos_per_tourn = {
            "agua": 2,
            "alimento": 2,
            "energia": 3,
            "comunicaciones": 3,
            "oxigeno": 1,
            "aceptacion": 1
        }
        for recurso, valor in recursos_per_tourn.items():
            self.recursos.modificar(recurso, valor)

    def estadisticas_mision(self):
        eventos_bien = self.eventos_procesados - self.eventos_mal_seleccionado
        return {
                    "Eventos procesados": self.eventos_procesados,
                    "Decisiones correctas": eventos_bien,
                    "Decisiones incorrectas": self.eventos_mal_seleccionado,
                    "Energia restante": self.estado_recurso("energia"),
                    "Agua restante": self.estado_recurso("agua"),
                    "Alimento restante": self.estado_recurso("alimento"),
                    "Comunicaciones restantes": self.estado_recurso("comunicaciones"),
                    "Oxigeno restante": self.estado_recurso("oxigeno"),
                    "Aceptacion restante": self.estado_recurso("aceptacion"),
                    "Puntuacion final": self.puntuacion,
                    "Indice de eficiencia": round((eventos_bien / self.eventos_procesados) * 100, 2) if self.eventos_procesados > 0 else 0,
                    "Estado final": self.estado 
                }

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "type": self.type,
            "estado": self.estado,
            "puntuacion": self.puntuacion,
            "turno": self.turno,
            "dificultad": self.dificultad,
            "eventos_procesados": self.eventos_procesados,
            "eventos_mal_seleccionado": self.eventos_mal_seleccionado,
            "historial": self.historial,
            "recursos": self.recursos.to_dict() if self.recursos else None,
            "recursos_iniciales": self.recursos_iniciales,
            "partida_finalizada": self.partida_finalizada
        }

    @classmethod
    def from_dict(cls, data):
        if not data: return None
        mision = cls(data["nombre"], data["descripcion"], data["type"])
        mision.estado = data["estado"]
        mision.puntuacion = data["puntuacion"]
        mision.turno = data["turno"]
        mision.dificultad = data["dificultad"]
        mision.eventos_procesados = data["eventos_procesados"]
        mision.eventos_mal_seleccionado = data["eventos_mal_seleccionado"]
        mision.historial = data["historial"]
        mision.recursos = recursos.Recursos.from_dict(data["recursos"])
        mision.recursos_iniciales = data.get("recursos_iniciales") or {}
        mision.partida_finalizada = data["partida_finalizada"]
        return mision


def generar_recursos_aleatorios() -> dict:
    return {
        "agua": rd.randrange(30, 91),
        "alimento": rd.randrange(30, 91),
        "energia": rd.randrange(20, 91),
        "comunicaciones": rd.randrange(20, 91),
        "oxigeno": rd.randrange(40, 96),
        "aceptacion": rd.randrange(30, 81),
    }


misiones_predefinidas = [
    {
        "nombre": "Colapso en Distrito Norte",
        "descripcion": "Una tormenta eléctrica dañó la red principal hace 6 horas. "
                        "Los sistemas de respaldo aguantan, pero el margen es estrecho.",
        "recursos": {
            "agua": 75,
            "alimento": 80,
            "energia": 40,
            "comunicaciones": 70,
            "oxigeno": 85,
            "aceptacion": 60,
        },
    },
    {
        "nombre": "Cuarentena en Puerto Sur",
        "descripcion": "Un brote de contaminación obligó a sellar el sector portuario. "
                        "Los suministros externos están cortados, pero la infraestructura "
                        "interna sigue intacta.",
        "recursos": {
            "agua": 30,
            "alimento": 45,
            "energia": 90,
            "comunicaciones": 85,
            "oxigeno": 70,
            "aceptacion": 50,
        },
    },
    {
        "nombre": "Apagón Total en Sector Este",
        "descripcion": "Una falla en cascada dejó fuera de línea casi toda la red "
                        "energética. La población empieza a inquietarse por la falta "
                        "de información oficial.",
        "recursos": {
            "agua": 60,
            "alimento": 65,
            "energia": 15,
            "comunicaciones": 20,
            "oxigeno": 90,
            "aceptacion": 35,
        },
    },
    {
        "nombre": "Refugio Sobrepoblado",
        "descripcion": "La llegada masiva de desplazados triplicó la demanda de "
                        "recursos básicos en cuestión de días. Todo está bajo presión, "
                        "nada está en crisis todavía.",
        "recursos": {
            "agua": 55,
            "alimento": 40,
            "energia": 65,
            "comunicaciones": 60,
            "oxigeno": 60,
            "aceptacion": 45,
        },
    },
    {
        "nombre": "Sistema Estable, Amenaza Latente",
        "descripcion": "Todo funciona con normalidad, pero los sensores detectan una "
                        "anomalía creciente en el suministro de oxígeno que aún no se "
                        "ha manifestado.",
        "recursos": {
            "agua": 85,
            "alimento": 85,
            "energia": 85,
            "comunicaciones": 80,
            "oxigeno": 50,
            "aceptacion": 75,
        },
    },
    {
            "nombre": "Random generate",
            "descripcion": "Partida inicializada con recursos aleatorios",
            "aleatorio": True,
            "recursos": generar_recursos_aleatorios(),
        }
]