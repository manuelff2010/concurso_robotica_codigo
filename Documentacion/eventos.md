recursos = agua, alimento, energia, communicaciones, oxigeno, aceptacion

1. Falla en la red energética

descripcion: una alta demanda de energia provoco un sobrecalentamiento de las bobinas de los generadores, derritiendo el revestimiento y generando un corto catastrofico!

Opción A: "Activar generadores de respaldo" (energía -5, aceptación +5, puntos +10, correcta)
Opción B: "Esperar reparación automática" (energía -25, aceptación -10, puntos -10)

2. Contaminación del agua
descripcion: el sistema de control de la presion fallo, los filtros se rompieron y liberaron los desechos filtrados al aguaa junto con sus restos.

Opción A: "Activar filtros de emergencia" (agua -5, comunicación -5, aceptación +5, puntos +10, correcta)
Opción B: "Racionar sin filtrar" (agua -20, alimentos -10, aceptación -15, puntos -10)

3. Pérdida de comunicaciones
descripncion: un pico de tension ha ocasionado, que la antena no pueda sintetizar correctamente las señales

Opción A: "Reiniciar antena satelital" (comunicación -10, energía -5, puntos +10, correcta)
Opción B: "Ignorar y seguir sin reportar" (comunicación -30, aceptación -10, puntos -15)

4. Fuga de oxígeno en el sector B
descripcion: un sector altamente poblado ha reportado fugas en los gaseoductos de oxigeno externos antiguos.

Opción A: "Sellar sector y redirigir suministro" (oxígeno -10, energía -5, aceptación +5, puntos +15, correcta)
Opción B: "Evacuar todo el sector" (oxígeno -5, alimentos -15, aceptación -10, puntos -5)

5. Escasez de alimentos por bloqueo de transporte
descripcion: las rutas y ciudades vecinas han colapsado, los transportadores reportan vias imposibles y gran numero de bandidos

Opción A: "Usar reservas de emergencia" (alimentos -10, puntos +10, correcta)
Opción B: "Reducir raciones sin plan" (alimentos -25, comunicación -5, aceptación -15, puntos -10)

6. Sobrecarga en el sistema central
descripcion: el sistema no puede procesar tantas peticiones por segundo, a sobrepasado su capacidad de procesamiento en el sector C

Opción A: "Redistribuir carga entre sectores" (energía -10, oxígeno -5, puntos +15, correcta)
Opción B: "Forzar el sistema al límite" (energía -30, aceptación -10, puntos -20 — puede disparar directo a CRÍTICA si el recurso queda muy bajo)

7. Motín/desconfianza del equipo
descripcion: tus colaboradores han empezado fuertes discusiones, sobre un distribucion de recursos equitativa.

Opción A: "Comunicar la situación con transparencia" (comunicación -5, aceptación +15, puntos +10, correcta)
Opción B: "Ocultar la gravedad de la crisis" (comunicación -15, aceptación -20, puntos -15)

8. Hallazgo de un depósito de suministros
descripcion: un grupo de investigadores ha detectado en el radar un punto de suministro en una de las ciudades colapsadas, se discute la presencia de recursos

Opción A: "Enviar equipo a recuperarlo" (energía -5, alimentos +20, agua +10, aceptación +5, puntos +15, correcta)
Opción B: "No arriesgar recursos en la expedición" (sin cambios, puntos +0 — neutral, no incorrecta)

9. Convoy de ayuda humanitaria llega antes de lo previsto
descripcion: una ciudad respondio a tu crisis con ayuda humanitaria, y ha llegado antes de lo que se esperaba

Opción A: "Coordinar la descarga y distribución ordenada" (alimentos +15, agua +10, aceptación +10, puntos +15, correcta)
Opción B: "Dejar que cada sector tome lo que pueda por su cuenta" (alimentos +5, comunicación -10, aceptación -10, puntos -5 — genera desorden aunque igual llegue algo)

10. Ingeniero de la ciudad ofrece reparar un generador viejo gratis
descripcion: un ingeniero refugiado se ha ofrecido a reparar un generador abandonado de forma gratuita.

Opción A: "Aceptar la ayuda y supervisar el trabajo" (energía +20, aceptación +5, puntos +10, correcta)
Opción B: "Rechazar por protocolo, preferir personal propio" (sin cambios, aceptación -5, puntos +0 — neutral, no aprovecha la oportunidad)

11. Se restablece parcialmente una torre de comunicación externa

descripcion: el equipo de cientificos logro conectarse a una torre cercana a la ciudad. aunque se desconoce su estado actual.

Opción A: "Aprovechar la ventana para sincronizar todos los reportes pendientes" (comunicación +20, aceptación +5, puntos +15, correcta)
Opción B: "Usarla solo para un mensaje breve y cortar" (comunicación +5, puntos +5 — no incorrecta, solo subóptima)

12. Voluntarios locales se ofrecen para purificar agua manualmente
descripcion: un grupo de voluntarios refugiados se ofrece a poder purificar el agua de un deposito cercano

Opción A: "Organizar turnos y aceptar la ayuda" (agua +15, oxígeno +5, aceptación +10, puntos +15, correcta)
Opción B: "Rechazar por falta de protocolo de seguridad certificado" (sin cambios, aceptación -5, puntos +0 — neutral)


Menu principal: 
    - inicio sesion
    - registro
    - cerrar

Menu de usuario:
    - nueva mision
    - misiones activas
    - config
    - cerrar sesion

misiones activas:
    - mision_1
    - mision-2
    etc.

Menu de nueva mision:
    - nombre
    - volver

selector de mision:
    - mision pre establecida 1
    - mision pre establecida 2
    - mision pre establecida 3
    - mision aleatoria
    - voler

Menu de juego:
    - turno actual: int
    - recursos
    - ejecutar simulacion
    - historial
    - volver

Menu recursos:
    - agua
    - energia
    - comunicaciones
    - oxigeno
    - aceptacion
    - volver
ejecutar simulacion:
    verifica si no hay eventos si no pasa a siguiente turno

Menu eventos:
    - evento 1
    - evento 2
    - evento 3
    - volver

menu sub evento:
    -descripcion
    - opcion A
    - opcion B

histortial:
    historial XD

finalizacion mision:
    - perdio o gano
    - generar reporte
    - estadicticas
    - replay
    - voler

MISIONES PREDEFINIDAS

1. "Colapso en Distrito Norte"
descripcion: Una tormenta eléctrica dañó la red principal hace 6 horas.
Los sistemas de respaldo aguantan, pero el margen es estrecho.
recursos iniciales:
    agua: 75
    alimento: 80
    energia: 40
    comunicaciones: 70
    oxigeno: 85
    aceptacion: 60

2. "Cuarentena en Puerto Sur"
descripcion: Un brote de contaminación obligó a sellar el sector portuario.
Los suministros externos están cortados, pero la infraestructura interna
sigue intacta.
recursos iniciales:
    agua: 30
    alimento: 45
    energia: 90
    comunicaciones: 85
    oxigeno: 70
    aceptacion: 50

3. "Apagón Total en Sector Este"
descripcion: Una falla en cascada dejó fuera de línea casi toda la red
energética. La población empieza a inquietarse por la falta de
información oficial.
recursos iniciales:
    agua: 60
    alimento: 65
    energia: 15
    comunicaciones: 20
    oxigeno: 90
    aceptacion: 35

4. "Refugio Sobrepoblado"
descripcion: La llegada masiva de desplazados triplicó la demanda de
recursos básicos en cuestión de días. Todo está bajo presión, nada está
en crisis todavía.
recursos iniciales:
    agua: 55
    alimento: 40
    energia: 65
    comunicaciones: 60
    oxigeno: 60
    aceptacion: 45

5. "Sistema Estable, Amenaza Latente"
descripcion: Todo funciona con normalidad, pero los sensores detectan
una anomalía creciente en el suministro de oxígeno que aún no se ha
manifestado. Ideal como punto de partida sin presión inicial.
recursos iniciales:
    agua: 85
    alimento: 85
    energia: 85
    comunicaciones: 80
    oxigeno: 50
    aceptacion: 75


MISIÓN ALEATORIA — rangos sugeridos para random.randint()

    agua:          entre 30 y 90
    alimento:      entre 30 y 90
    energia:       entre 20 y 90
    comunicaciones: entre 20 y 90
    oxigeno:       entre 40 y 95
    aceptacion:    entre 30 y 80