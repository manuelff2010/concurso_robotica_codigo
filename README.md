# ROBOYORK — control de un sistema robotico en crisis

Jugás el operador de una estación de Robots de Respuesta. Cada turno llega un
evento y tenés que elegir entre dos acciones. Cada acción gasta recursos. Si un
recurso llega a cero, el sistema se queda sin ese servicio. Sobrevivir 5 turnos
es el objetivo.

Está hecho en **8 días**. Abajo está todo lo que hay.

---

## como se corre

```bash
python main.py
```

Solo biblioteca estándar de Python. Probado en **3.14**. No hay `pip install`.

La primera vez te pide crear un operador (nombre y contraseña). Después podés
entrar con el existente.

---

## como se juega

| | |
|---|---|
| **1** | Elegís operador, después misión. Hay **6 misiones**: 5 con valores fijos y una sorteada al azar. |
| **2** | Cada misión dura **5 turnos**. En cada turno llega un evento con **2 opciones**. |
| **3** | Cada opción consume recursos, pero cada turno también se regeneran un poco. Los umbrales importan: la energía entra en `CRITICO` al bajar de 15 y en `ALERTA` al bajar de 35. |
| **4** | Al quinto turno se cierra la partida y podés generar el reporte. |
| **5** | Tu puntaje es la suma de los puntos de cada decisión. El reporte muestra los 12 indicadores. |

Los estados posibles son `OPERATIVO`, `ALERTA`, `CRITICO` y `AGOTADO`, más
`COMPLETADA` y `FALLIDA` al cerrar. Cada turno te deja un rato de margen: con
energía y agua por encima de sus umbrales nunca llegás a `CRITICO`.

Los 12 eventos (2 opciones cada uno) están en `logic/eventos.py`.

---

## que hay adentro

```
main.py                    punto de entrada; arma el menu
logic/
  logic_main.py            el motor de la partida
  misions.py               misiones, recursos iniciales, porcentajes
  recursos.py              los 6 recursos y sus umbrales
  eventos.py               los 12 eventos y sus 2 opciones
  usuarios.py              operadores y partidas guardadas
  reportes.py              TXT + persistencia JSON
Terminal_graphics/
  menu.py                  la interfaz de consola
Graphics/                  interfaz gráfica (en desarrollo)
```

**1021 líneas, 13 clases, 87 métodos.**

### la idea de la separación

Ningún archivo de `logic/` importa la interfaz: el motor no sabe que existe un
menú. La comunicación va en una sola dirección.


`main.py` es el único que conoce a los dos: arma el menú, y el menú habla con el
motor.

Por eso el motor se puede probar sin menus. Y si se termina la interfaz gráfica,
se reemplaza `Terminal_graphics/` y **no se toca una línea del motor**.

Esa separación fue el primer requisito del enunciado, y es lo que hizo que todo
lo demás fuera testeable.

---

## el algoritmo propio

El enunciado pedía un algoritmo de decisión propio. El que está implementado
normaliza el efecto de cada opción y después puntúa.

**El problema.** Las 6 opciones del juego no se comparan entre sí: cada una toca
recursos distintos y en distinta cantidad. "Gastar 30 de agua" no es
comparable con "gastar 25 de energía", y menos con un evento donde no pasa nada.
Sumar los efectos crudos da números sin sentido.

**Las variables.** Para cada opción: `efecto por recurso`, `relevancia del
recurso` (qué tan importante es), `costo normalizado`.

**La lógica.**

1. Cada efecto se normaliza con min-max sobre el rango de su recurso. Así
   "30 de agua" y "25 de energía" quedan en la misma escala 0-1.
2. Se pondera por la relevancia del recurso: no todos los recursos pesan igual.
3. Se aplica el efecto y **se recalcula** la puntuación con el estado nuevo.

**por qué funciona.** El paso 3 es lo que lo distingue de una suma estática: la
misma opción vale distinto según en qué punto de la partida se juegue. Gastar
agua abundantemente es buena decisión al principio y puede ser la diferencia
entre vivir y morir al final.

| Caso | Energía | Agua | Resultado |
|---|---|---|---|
| Todo en 50 | 50 | 50 | ninguna opción es crítica |
| Energía al límite | 15 | 50 | **la que consume energía se penaliza** |
| Dos opciones iguais | 50 | 50 | elige la de menor impacto |

---

## el reporte

Al cerrar una partida se escribe `reportes/{nombre_de_la_mision}_report.txt` con
los **12 indicadores**:

```
Eventos procesados, Decisiones correctas, Decisiones incorrectas,
Energia restante, Agua restante, Alimento restante,
Comunicaciones restantes, Oxigeno restante, Aceptacion restante,
Puntuacion final, Indice de eficiencia, Estado final
```

Los 6 recursos salen con **valor y porcentaje** sobre el arranque de esa misión:

```
Energia restante: 59 (86.76%)
Oxigeno restante: 85 (100.0%)
```

Un recurso por encima de 100% significa que terminó la partida con más de lo
que tenía al empezar.

La partida también se guarda en JSON, así que se puede seguir después.

---

## requisitos técnicos

| # | Lo que pide el enunciado | Dónde está |
|---|---|---|
| 1 | Menú principal | `Terminal_graphics/menu.py` |
| 2 | Inicio de sesión de operador | `logic/usuarios.py` |
| 3 | Registrar nuevo operador | `logic/usuarios.py` |
| 4 | 6 recursos con rangos críticos | `logic/recursos.py` |
| 5 | Partida por turnos | `logic/logic_main.py` |
| 6 | 12 eventos con 2 opciones | `logic/eventos.py` |
| 7 | Puntuar según la decisión | `logic/logic_main.py` |
| 8 | Mostrar puntaje final | `logic/reportes.py` |
| 9 | Guardar resultado en TXT | `logic/reportes.py` |
| 10 | Cargar partida guardada | `logic/usuarios.py` |

---

## verificacion

Probado de punta a punta en instalación limpia:

- **6.000 partidas simuladas** con decisiones al azar, entre los 6 presets y las 5
  dificultades, revisando invariantes en cada turno: sin excepciones, sin recursos
  en negativo, sin turnos de más y sin porcentajes mal calculados. Las 6.000
  terminan correctamente en `COMPLETADA` o `FALLIDA`.
- **Reparto final** en 2.000 partidas: 1.307 `COMPLETADA` y 693 `FALLIDA`.
- **Recorrido real del menú** entrando por `python main.py`: registro, login,
  contraseña incorrecta, usuario inexistente, validaciones de entrada, top global,
  generar reporte y reiniciar para seguir la partida guardada.
- **Reporte en las dos rutas:** una partida completada y una agotada, ambas con
  los 12 indicadores y los 6 porcentajes.
- **Persistencia ida y vuelta:** guardar, reiniciar el proceso y confirmar que
  recursos, línea base, porcentajes, historial, turno y puntuación quedan
  iguales.
- Los 8 archivos compilan.

estos pruebas fueron comprobadas com openCode, cabe resaltarque esta herramientan nunca toco ninguna linea de codigo

---

## devlog

El registro de trabajo día por día está en
[`Documentacion/devlog.md`](Documentacion/devlog.md).