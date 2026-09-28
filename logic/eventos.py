import random as rd

class Opcion():
    def __init__(self, is_correct: bool, title: str, causa: tuple):
       self.is_correct = is_correct
       self.title = title
       self.consecuences = causa
        
class Event():
    def __init__(self, name: str, description: str, opciones: list[Opcion]):
       self.name = name
       self.descripcion = description
       self.opciones = opciones
    def activate(self, option):
       return self.opciones[option].consecuences
 
eventos = [
    Event("Falla en la red energética",
          "Una alta demanda de energía provocó un sobrecalentamiento de las bobinas de los generadores, derritiendo el revestimiento y generando un corto catastrófico.",
          [
              Opcion(True, "Activar generadores de respaldo",
                     {"energia": -5, "aceptacion": 5, "puntos": 10}),
              Opcion(False, "Esperar reparación automática",
                     {"energia": -25, "aceptacion": -10, "puntos": -10}),
          ]),
 
    Event("Contaminación del agua",
          "El sistema de control de la presión falló, los filtros se rompieron y liberaron los desechos filtrados al agua junto con sus restos.",
          [
              Opcion(True, "Activar filtros de emergencia",
                     {"agua": -5, "comunicaciones": -5, "aceptacion": 5, "puntos": 10}),
              Opcion(False, "Racionar sin filtrar",
                     {"agua": -20, "alimento": -10, "aceptacion": -15, "puntos": -10}),
          ]),
 
    Event("Pérdida de comunicaciones",
          "Un pico de tensión ha ocasionado que la antena no pueda sintetizar correctamente las señales.",
          [
              Opcion(True, "Reiniciar antena satelital",
                     {"comunicaciones": -10, "energia": -5, "puntos": 10}),
              Opcion(False, "Ignorar y seguir sin reportar",
                     {"comunicaciones": -30, "aceptacion": -10, "puntos": -15}),
          ]),
 
    Event("Fuga de oxígeno en el sector B",
          "Un sector altamente poblado ha reportado fugas en los gaseoductos de oxígeno externos antiguos.",
          [
              Opcion(True, "Sellar sector y redirigir suministro",
                     {"oxigeno": -10, "energia": -5, "aceptacion": 5, "puntos": 15}),
              Opcion(False, "Evacuar todo el sector",
                     {"oxigeno": -5, "alimento": -15, "aceptacion": -10, "puntos": -5}),
          ]),
 
    Event("Escasez de alimentos por bloqueo de transporte",
          "Las rutas y ciudades vecinas han colapsado, los transportadores reportan vías imposibles y gran número de bandidos.",
          [
              Opcion(True, "Usar reservas de emergencia",
                     {"alimento": -10, "puntos": 10}),
              Opcion(False, "Reducir raciones sin plan",
                     {"alimento": -25, "comunicaciones": -5, "aceptacion": -15, "puntos": -10}),
          ]),
 
    Event("Sobrecarga en el sistema central",
          "El sistema no puede procesar tantas peticiones por segundo, ha sobrepasado su capacidad de procesamiento en el sector C.",
          [
              Opcion(True, "Redistribuir carga entre sectores",
                     {"energia": -10, "oxigeno": -5, "puntos": 15}),
              Opcion(False, "Forzar el sistema al límite",
                     {"energia": -30, "aceptacion": -10, "puntos": -20}),
          ]),
 
    Event("Motín/desconfianza del equipo",
          "Tus colaboradores han empezado fuertes discusiones sobre una distribución de recursos equitativa.",
          [
              Opcion(True, "Comunicar la situación con transparencia",
                     {"comunicaciones": -5, "aceptacion": 15, "puntos": 10}),
              Opcion(False, "Ocultar la gravedad de la crisis",
                     {"comunicaciones": -15, "aceptacion": -20, "puntos": -15}),
          ]),
 
    Event("Hallazgo de un depósito de suministros",
          "Un grupo de investigadores ha detectado en el radar un punto de suministro en una de las ciudades colapsadas, se discute la presencia de recursos.",
          [
              Opcion(True, "Enviar equipo a recuperarlo",
                     {"energia": -5, "alimento": 20, "agua": 10, "aceptacion": 5, "puntos": 15}),
              Opcion(False, "No arriesgar recursos en la expedición",
                     {"puntos": 0}),
          ]),
 
    Event("Convoy de ayuda humanitaria llega antes de lo previsto",
          "Una ciudad respondió a tu crisis con ayuda humanitaria, y ha llegado antes de lo que se esperaba.",
          [
              Opcion(True, "Coordinar la descarga y distribución ordenada",
                     {"alimento": 15, "agua": 10, "aceptacion": 10, "puntos": 15}),
              Opcion(False, "Dejar que cada sector tome lo que pueda por su cuenta",
                     {"alimento": 5, "comunicaciones": -10, "aceptacion": -10, "puntos": -5}),
          ]),
 
    Event("Ingeniero de la ciudad ofrece reparar un generador viejo gratis",
          "Un ingeniero refugiado se ha ofrecido a reparar un generador abandonado de forma gratuita.",
          [
              Opcion(True, "Aceptar la ayuda y supervisar el trabajo",
                     {"energia": 20, "aceptacion": 5, "puntos": 10}),
              Opcion(False, "Rechazar por protocolo, preferir personal propio",
                     {"aceptacion": -5, "puntos": 0}),
          ]),
 
    Event("Se restablece parcialmente una torre de comunicación externa",
          "El equipo de científicos logró conectarse a una torre cercana a la ciudad, aunque se desconoce su estado actual.",
          [
              Opcion(True, "Aprovechar la ventana para sincronizar todos los reportes pendientes",
                     {"comunicaciones": 20, "aceptacion": 5, "puntos": 15}),
              Opcion(False, "Usarla solo para un mensaje breve y cortar",
                     {"comunicaciones": 5, "puntos": 5}),
          ]),
 
    Event("Voluntarios locales se ofrecen para purificar agua manualmente",
          "Un grupo de voluntarios refugiados se ofrece a poder purificar el agua de un depósito cercano.",
          [
              Opcion(True, "Organizar turnos y aceptar la ayuda",
                     {"agua": 15, "oxigeno": 5, "aceptacion": 10, "puntos": 15}),
              Opcion(False, "Rechazar por falta de protocolo de seguridad certificado",
                     {"aceptacion": -5, "puntos": 0}),
          ]),
]