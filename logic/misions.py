from logic import recursos
import random as rd

class Mision():
    
    def __init__(self, nombre: str, descripcion: str, type: str):
        self.type = type
        self.nombre = nombre
        self.estado = "INICIALIZADO"
        self.descripcion = descripcion
        self.puntuacion = 0
        self.turno = 0
        self.eventos_procesados = 0
        self.eventos_mal_seleccionado = 0
        self.historial = []
        self.historial.append(f"mision {self.nombre} inicializada")
        self.historial.append(f"mision: {self.descripcion}")
    
    def sources_init(self, recursoso_iniciales: dict):
        self.recursos = recursos.Recursos(recursoso_iniciales)
        self.historial.append(f"recursos iniciales: ")
        for nombre in self.recursos.estados().keys():
            self.historial.append(f"{nombre}: {self.recursos.obtener(nombre)}")
    
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
            "recursos": {
                "agua": rd.randrange(30, 91),
                "alimento": rd.randrange(30, 91),
                "energia": rd.randrange(20, 91),
                "comunicaciones": rd.randrange(20, 91),
                "oxigeno": rd.randrange(40, 96),
                "aceptacion": rd.randrange(30, 81),
            },
        }
]