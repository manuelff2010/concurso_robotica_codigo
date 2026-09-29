class Recursos:
    def __init__(self, recursos):
        self._valores = recursos.copy()
        self.UMBRALES = {
            "energia":        {"alerta": 35, "critico": 15},
            "comunicaciones": {"alerta": 35, "critico": 15},
            "agua":           {"alerta": 30, "critico": 12},
            "alimento":       {"alerta": 30, "critico": 12},
            "aceptacion":     {"alerta": 25, "critico": 10},
            "oxigeno":        {"alerta": 15, "critico": 5},
        }
    def obtener(self, nombre):
        return self._valores[nombre]

    def modificar(self, nombre, cambio):
        self._valores[nombre] = self._valores[nombre] + cambio 

    def estados(self):
        resultado = {}
        for recurso, valor in self._valores.items():
            umbral = self.UMBRALES[recurso]
            if valor <= 0:
                resultado[recurso] = "AGOTADO"
            elif valor < umbral["critico"]:
                resultado[recurso] = "CRITICO"
            elif valor < umbral["alerta"]:
                resultado[recurso] = "ALERTA"
            else:
                resultado[recurso] = "OPERATIVO"
        return resultado
    
    def estado_general(self):
        agotados = 0
        criticos = 0
        alertas = 0
        for i in self.estados().values():
            if i == "AGOTADO":
                agotados += 1
            elif i == "CRITICO":
                criticos += 1
            elif i == "ALERTA":
                alertas += 1
        
        if agotados > 0:
            return "AGOTADO"
        elif criticos > 0 or alertas > 2:
            return "CRITICO"
        elif alertas == 1 or alertas == 2:
            return "ALERTA"
        else:
            return "OPERATIVO"
        