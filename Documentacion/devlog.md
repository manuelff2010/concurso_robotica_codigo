## [24/09/26] — Día 1

Hoy tuve un problema para poder acceder al documento, asique decidi tomarlo para poder planificar bien mis ideas antes de escribir lineas
dado que es algo con lo que he trabajado antes y me gusta quiero pensar en el apartado grafico, quiero tenerlo fuera de terminal y si sobre tiempo hacerlo adaptable tanto como para terminal como graficamente, ademas de empezar a pensar como llevar la documentacion, el estilo que quiero para el proyecto, y reflexionar como podria estructurarlo.

por lo tanto lo interesante de hoy fue la eleccion de la libreria grafica, y el diseño, dado que la situacion planteada se ambienta en 2040 decidi elergir el estilo cyberpunk futurista, con mucha tecnologia y estilo. con el diseño claro, de experiencias previas tkinter es muy feo y engorroso sobre todo para la estetica que busco, pense en usar pygame, una libreria con la que he trabajado multiples veces y es muy flexible sin embargo ese mismo control hace que hacer cosas como botones sea largo, que en 8 dias no parece viable, por lo que pense en QT que nunca he trabajado o otras alternativas.

QT tiene una curva larga, imposible en 8 dias!! aunque en mi busca de con dearpygui un estilo y una sintaxis mas amigable, ademas de customtkinter una con lo que trabaje pocas veces antes, aunque comparando techos de dificultad, y mi ligero odio por tkinter, decidi dearpygui.
hoy fue un dia de buscar codigos de ejemplo, construir cosas basicas, y buscar como programar cosas que tuviera pensadas para el estilo cyberpunk.

por el lado de la documentacion, no tengo mucha experiencia, pero dado lo que pedian de explicar desiciones tecnicas y demas, y ya habia lelvado un diario de programador en el pasado me parecio perfecto para esto, esta seccion un poco mas del dia a dia explicando mi perspectiva.
con un pulido minimo, y posteriormente terminado el proyecto un README en condiciones con todo bien estructurado y pulido.

Mañana quiero empezar con la logica, lo fundamental antes de tocar la parte grafica que es un extra, que sea modular, mas similar a una libreria de importacion dado que si quiero tenerlo grafico y talvez adaptarlo a terminal tambien, y por como pide el proyecto tiene que quedar bien separada. y en este momento escribiendo creo que seria increible aprender a hacer bitacoras mas resumidas.

## [25/09/26] — Día 2

hoy experimente mucho con la libreria, tuve algunos errores tontos que consumieron tiempo, aunque al final logre un login medianamente decente, realmente me cuestiono si quedarme con customtkinter, aunque creo que puedo lograr un mejor resultado con esto. decidi tomarme un descanso despues de todo no es lo primordial del desafio, me puse con el gestor de recursos
al principio peque un poco intentando hacerlo con setter y properties pero quedaba largo, la mejor fue con un diccionario, y agregamos un check de lo que piden.

voy a centrarme en terminal la logica hacia sea en terminal antes de seguir, uso dos recursos extras, oxigeno, ya que me lo imagino como cupula o asi, y la aceptacion de los ciudadanos.
programo los clases de los eventos mientras pienso cada evento, realmente no se si estaba o no me acuerdo de cuantos eran, con 10 o 15 estara bien supongo.

para mañana me gustaria tener toda la logica basica terminada, realmente creo que me consumira mucho tiempo la parte grafica y la documentacion asique lo mejor sera ir sobradito.

## [26/09/26] — Día 3

hoy no tuve mucho tiempo en invertir, empeza a crear una interfaz fea y basica en terminal para empezar a encontrar los errores dentro de el logic main que es el encargado de gestionar toda la parte logica de forma que la implementacion ya sea grafica o por temrinal sea por medio de ver las variables internas y pasarle los datos de la interfaz, ademas de dejar precosntruidos los eventos en una lista, aunque probablemente modifique las consecuencias a posterior.

bueno esto redactado cerca de terminar el dia, escribi una clase rapida que permitiria hacer los menus de forma ligeramente mas comoda y corta, ademas de dejar algunos de los menus para la interfaz de terminal pre-establecidos lo que deberia facilitar mucho todo a posterior.

mañana me gustaria, dejar todo lo basico terminado de forma que el desafio quede tecnicamente terminado, para poder empezar mi tiempo en una documentacion solida y poder dedicar tiempo a la interfaz grafica y los demas desafios avanzado, tengo algo de miedo de los demas espero ir bien, todo tiene un poco mas de lo que pide el documento, mas recursos, mas eventos. en fin espero mañana poder terminar las cosas basicas del proyecto y yo creo que hare en commit y un repositorio en github, me esta gustando como me esta quedando, me pregunto si alguien leera esto.

## [27/09/26] — Día 4

el dia de la furia, hoy empeze desde temprano para poder avanzar lo que queria hacer el dia anterior, si embargo creo que intente hacer las cosas muy complejas con un sitema de menus enlazados y demas, que al final se hizo demasiado complejo debido a los distintos propositos entre menus, devueltas y demas, en fin 2 horas a la basura, al fina llegue a una solucion relativamente elegante en el la propia clase de menus donde todos se hiban bateando entre si sin bucle, aunque con algo muy largo terminara colapsando por tantas llamadas, asique lo mejor seria que en vez de llamarlas.

cambien una variable y que con la variable sean llamadas desde un bucle y ellas puedan terminar correctamente sin llamar a otra, es lo mejor, por otra parte ya estoy con interfaces de terminal que creo que estan muy pulidas, aunque de momento voy hasta misiones, me falta aun una parte, ya deje 5 misiones pre definidas junto con una que genera lso recursos al azar dentro de una rangos, y creo que ya todo esta relativamente rapido, ademas de ir agregando las cosas que creo a un md que originalmente era solo apra los eventos pero ahurita tiene mas cosas que creo que podrian ayudar despues con la documentacion.

arregle varios bugs, estoy algo preocupado por que el documento pide con respectivos testeos, y yo lo hago sobre la marcha no se si se pone asi o teca diseñar estos cosas de test que prueban funciones que nunca he hecho, aun quedan algo de tiempo asique hare alguna cosa mas

## [28/09/26] — Día 5

hoy llegue y me enfoque rapido, acabe casi toda la logica simple, falta la parte de estadisticas, historial, y el reporte pero ya el resto esta completo aunque se rompio un poco con el arreglo de bugs creo que ahora esta decente, arregle detalles, aun me faltan algunos, que arreglare mañana que son relativamente menores mas de calidad de codigo y que quede bien con lo que pide la presentacion, dejando el codigo relativamente pulido para refactorizarlo ya que aunque ahurita funciona menu y logic main quedaron mu ycargados de responsabilidades que no les pertenezen, ademas de eso di varios pasos al frente en cuanto a una documentacion detallada, explica las bases de todo lo que tengo ahurita aunque es probable que cambie es una buena base de cual mejorar.

ya con el codigo mas limpio, arreglado de bugs y factorizado, que no creo que me demore mucho, la factorizacion la voy a hacer ligera, logic y menu quedaran algo cargados pero no creo que tenga mucho tiempo si me sobra lo hare, de hya termina la poca logica que falta, historial, estadisticas que son rapidas, y reporte que no entiendo bien como es, de hay volver a dejar el codigo bien bien bonito, para ya tener lo minimo que entregar, y ya podria concentrarme en los desafios avanzados con comodidad, aunque creo qeu ya cumplo algunos ademas de tener mas de las cosas que piden, pero nose, simplemente espero llegar tengo miedo de que alguien entregue algo mejor.

## [29/09/26] — Día 6

hoy no tuve tampoco mucho timepo para programar, aunque termine los historiales que se guardaran en una lista, las estadisticas estan como a un 50% tecniamente las da pero no con porcentajes como pide el documento, por otra parte recibi que al parecer no eran 8 dias si no mas tiempo hasta el 5 de oct, asique creo que tecnicamente voy bastante bien, ya no se ve tan lejana la posibilidad de hacerlo grafico aunque me gusta como se ve en terminal, creo que ha sido mi aplicacion de terminal mas pulida sobre todo que me gusto como quedo la navegacion, pero bueno igual yo creo que haria todos los desafios dificiles antes que ese, voy a terminar de arreglar el codigo para que quede organizado como se debe, sente las bases para el manejo de .txt para historial y asi y json para configuracion si es que la hago, pero dado que creo que implementarlo cambiaria mucho el codigo quiero refactorizarlo antes de hacer eso, ademas creo que para el reporte voy a hacer que lo de en un pdf, quiero decir encontre una libreria que hace que aunque algo tedioso, no se ve muy complejo o distinto a lo que ya hay con los txt, y siento que queda mucho mas profesional.
