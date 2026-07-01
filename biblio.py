
#FUNCIONES DE VALIDACIÓN


def validar_titulo(titulo):
    
    return titulo.strip() != ""


def validar_copias(copias):
    
    # copias.isdigit() verifica que TODOS los caracteres del
    # texto sean dígitos (0-9). Si hay letras, espacios, signo
    # "-" o un punto decimal, isdigit() ya retorna False y la
    # función corta aquí gracias al operador "and" (no sigue
    # evaluando la segunda condición).
    # Si pasa esa prueba, se convierte a int() y se exige >= 0.
    return copias.isdigit() and int(copias) >= 0


def validar_prestamo(prestamo):
    # "prestamo" (parámetro): el texto ingresado para los días
    # de préstamo. Se llama así porque representa el período
    # de préstamo del libro, en días.
    #
    # Misma lógica que validar_copias, pero el préstamo debe
    # ser estrictamente mayor que cero (> 0), porque un
    # préstamo de 0 días no tiene sentido.
    return prestamo.isdigit() and int(prestamo) > 0


# ------------------------------------------------------------
# FUNCIONES DEL MENÚ
# ------------------------------------------------------------

def mostrar_menu():
    # Esta función no recibe ni guarda ninguna variable.
    # Su único trabajo es imprimir texto fijo en pantalla.
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar libros")
    print("6. Salir")
    print("====================================")


def leer_opcion():
    # "while True" crea un ciclo infinito que solo se detiene
    # cuando algo dentro de él ejecuta un "return" o "break".
    while True:
        # "opcion" (variable LOCAL de esta función, distinta
        # de cualquier otra "opcion" que aparezca más abajo en
        # el archivo): guarda el TEXTO que el usuario escribió
        # al elegir una opción del menú. Todavía es texto, no
        # número, porque input() siempre devuelve texto.
        opcion = input("Seleccione una opción: ")

        # "opcion.isdigit()" comprueba que ese texto sean solo
        # dígitos. "1 <= int(opcion) <= 6" es una comparación
        # encadenada de Python: equivale a escribir
        # "int(opcion) >= 1 and int(opcion) <= 6" pero en una
        # sola expresión más legible. Aquí "int(opcion)"
        # convierte el texto a número solo para comparar,
        # sin guardar ese número en ninguna variable nueva.
        if opcion.isdigit() and 1 <= int(opcion) <= 6:
            # "return int(opcion)" hace dos cosas a la vez:
            # convierte el texto "opcion" a número entero,
            # y entrega ese número como resultado de la función,
            # saliendo de ella inmediatamente.
            return int(opcion)
        else:
            # Si no es válida, se informa el error y el
            # "while True" vuelve al inicio, pidiendo de nuevo
            # la opción (efecto de "reintentar hasta que sea
            # correcta").
            print("Opción inválida. Intente nuevamente.")


# ------------------------------------------------------------
# OPCIÓN 1: AGREGAR LIBRO
# ------------------------------------------------------------

def agregar_libro(lista):
    # "lista" (parámetro de la función): es la colección
    # completa de libros (la misma variable "libros" que
    # existe más abajo en el archivo, pero aquí adentro de la
    # función se llama "lista" porque es un nombre más
    # genérico). Llega por REFERENCIA: cualquier modificación
    # que se haga aquí dentro (como un .append) afecta
    # directamente a la lista original de afuera.

    # "titulo" (variable LOCAL de esta función): guarda el
    # texto que el usuario escribe para el nombre del libro.
    titulo = input("Ingrese título del libro: ")
    if not validar_titulo(titulo):
        # "not validar_titulo(titulo)" invierte el resultado:
        # si la validación dio False (título inválido),
        # "not False" es True, así que se entra a este bloque.
        print("El título no puede estar vacío.")
        # "return" sin ningún valor termina la función aquí
        # mismo, sin llegar a crear ni agregar el libro.
        return

    # Si llegamos a esta línea, es porque el "return" anterior
    # NO se ejecutó (el título era válido).
    #
    # "copias" (variable LOCAL): guarda el texto que el
    # usuario escribe para la cantidad de copias. Sigue siendo
    # texto en este punto, todavía no se ha convertido a número.
    copias = input("Ingrese cantidad de copias: ")
    if not validar_copias(copias):
        print("Las copias deben ser un número entero >= 0.")
        return

    # "prestamo" (variable LOCAL): guarda el texto que el
    # usuario escribe para los días de préstamo. Igual que
    # "copias", todavía es texto aquí.
    prestamo = input("Ingrese período de préstamo (días): ")
    if not validar_prestamo(prestamo):
        print("El período debe ser un número entero > 0.")
        return

    # Solo se llega hasta aquí si las TRES validaciones
    # pasaron sin activar ningún "return" anterior.
    #
    # "libro" (variable LOCAL): guarda un DICCIONARIO, es
    # decir, un solo registro con 4 datos relacionados entre
    # sí (el "ficha" de un libro individual). Se llama "libro"
    # en singular porque representa a UN libro, a diferencia
    # de "lista"/"libros" que representan la colección completa.
    libro = {
        "titulo": titulo.strip(),      # se guarda ya limpio de espacios
        "copias": int(copias),         # AQUÍ es donde "copias" pasa de texto a número
        "prestamo": int(prestamo),     # AQUÍ es donde "prestamo" pasa de texto a número
        "disponible": False            # siempre False al crear el libro;
                                        # nunca se le pide esto al usuario
    }

    # .append() agrega el diccionario "libro" (el registro que
    # acabamos de armar) al final de "lista" (la colección
    # completa que llegó como parámetro).
    lista.append(libro)

    print(f"Libro '{titulo.strip()}' agregado correctamente.")



# OPCIÓN 2: BUSCAR LIBRO
# (también es reutilizada por la opción 3, Eliminar libro)

def buscar_libro(lista, titulo):
    # "lista" (parámetro): la colección completa de libros,
    # recibida desde afuera para poder recorrerla aquí dentro.
    # "titulo" (parámetro): el texto que se quiere buscar.
    # Nota: este "titulo" es independiente del "titulo" que
    # existe dentro de agregar_libro; son variables distintas
    # aunque tengan el mismo nombre, porque cada una vive
    # solo dentro de su propia función.

    # enumerate(lista) recorre la lista entregando en cada
    # vuelta DOS valores a la vez:
    # "i" (variable LOCAL del for): el número de posición
    #     dentro de la lista (0, 1, 2, 3...).
    # "libro" (variable LOCAL del for): el diccionario completo
    #     que está en esa posición "i" durante esta vuelta.
    for i, libro in enumerate(lista):
        # Se compara el título ya guardado dentro del
        # diccionario (libro["titulo"], limpio porque se guardó
        # con .strip() en agregar_libro) contra el título de
        # búsqueda (el parámetro "titulo" de esta función,
       
        if libro["titulo"] == titulo.strip():
            # En cuanto encuentra una coincidencia, "return i"
            # sale de la función inmediatamente con la posición
            # donde se encontró.
            return i

    # Si el "for" terminó de recorrer toda la lista sin que
    # ningún "return i" se ejecutara, significa que no se
    # encontró el libro. Esta línea solo se alcanza en ese caso.
    return -1

# OPCIÓN 3: ELIMINAR LIBRO
def eliminar_libro(lista):
    # "lista" (parámetro): la colección completa de libros.

    # "titulo" (variable LOCAL): el texto que el usuario
    # escribe indicando qué libro quiere eliminar.
    titulo = input("Ingrese el título del libro a eliminar: ")

    # "pos" (variable LOCAL, abreviatura de "posición"): guarda
    # el número que retorna buscar_libro. Puede ser un índice
    # válido (0, 1, 2...) si el libro existe, o -1 si no se
    # encontró ningún libro con ese título.
    #
    # En vez de volver a escribir la lógica de búsqueda, se
    # reutiliza la función ya creada para la opción 2.
    pos = buscar_libro(lista, titulo)

    if pos != -1:
        # "lista.pop(pos)" elimina el elemento que está
        # exactamente en la posición guardada en "pos" y lo
        # quita de la lista de forma permanente.
        lista.pop(pos)
        print(f"Libro '{titulo.strip()}' eliminado.")
    else:
        # pos == -1 significa que buscar_libro no encontró
        # ningún libro con ese título.
        print(f"El libro '{titulo}' no se encuentra registrado.")


# OPCIÓN 4: ACTUALIZAR DISPONIBILIDAD

def actualizar_disponibilidad(lista):
    # "lista" (parámetro): la colección completa de libros.

    # "libro" (variable LOCAL del for): en cada vuelta del
    # ciclo, contiene el diccionario de UN libro distinto de
    # la lista (no su posición esta vez, solo el diccionario).
    for libro in lista:
        # "libro["copias"] >= 1" ya es una expresión que vale
        # True o False directamente, así que se puede asignar
        # tal cual al campo "disponible" sin necesidad de un
        # if/else explícito.
        # Como "libro" es una referencia al diccionario real
        # (no una copia), este cambio queda reflejado
        # directamente en la lista original que llegó como
        # parámetro.
        libro["disponible"] = libro["copias"] >= 1


# OPCIÓN 5: MOSTRAR LIBROS

def mostrar_libros(lista):
    # "lista" (parámetro): la colección completa de libros.

    # Antes de mostrar nada, se asegura de que el campo
    # "disponible" de todos los libros esté actualizado.
    actualizar_disponibilidad(lista)

    print("=== LISTA DE LIBROS ===")

    # "libro" (variable LOCAL del for): el diccionario de un
    # libro distinto en cada vuelta del ciclo.
    for libro in lista:
        # "estado" (variable LOCAL): guarda el texto
        # "DISPONIBLE" o "SIN COPIAS" según el valor de
        # libro["disponible"]. Se llama "estado" porque
        # describe la situación actual del libro en ese
        # momento de la ejecución.
        #
        # Esto es un operador condicional ternario: una forma
        # compacta de escribir, en una sola línea, lo
        # equivalente a:
        #   if libro["disponible"]:
        #       estado = "DISPONIBLE"
        #   else:
        #       estado = "SIN COPIAS"
        estado = "DISPONIBLE" if libro["disponible"] else "SIN COPIAS"

        print(f"Título: {libro['titulo']}")
        print(f"Copias: {libro['copias']}")
        print(f"Préstamo: {libro['prestamo']}")
        print(f"Estado: {estado}")
        print("********************************************")


# "libros" (variable GLOBAL, en plural porque guarda la
# colección COMPLETA, no un solo libro): se crea UNA SOLA VEZ,
# vacía, antes de que empiece el menú. Va a persistir y crecer
# durante toda la ejecución del programa, ya que vive en el
# archivo completo y no dentro de ninguna función.
libros = []

while True:
    mostrar_menu()

    # "opcion" (variable GLOBAL en este punto, distinta de la
    # "opcion" que existe DENTRO de la función leer_opcion():
    # esa era local a su propia función y ya dejó de existir
    # en cuanto esa función terminó). Esta "opcion" de aquí
    # guarda el NÚMERO entero (entre 1 y 6) que devuelve
    # leer_opcion(), ya validado y convertido.
    opcion = leer_opcion()

    if opcion == 1:
        # Se le pasa "libros" para que, dentro de la función,
        # se reciba como el parámetro "lista" y pueda
        # modificarse directamente con .append().
        agregar_libro(libros)

    elif opcion == 2:
        # "titulo" (variable GLOBAL en este bloque): el texto
        # que el usuario escribe para buscar un libro.
        titulo = input("Ingrese el título a buscar: ")

        # "pos" (variable GLOBAL en este bloque): guarda la
        # posición que retorna buscar_libro, o -1 si no existe.
        pos = buscar_libro(libros, titulo)

        if pos != -1:
            # Es AQUÍ, en este bloque principal, donde se
            # decide qué hacer con el resultado de la búsqueda
            # (no dentro de buscar_libro, que solo retorna la
            # posición, sin imprimir nada).
            #
            # "libro" (variable GLOBAL en este bloque): el
            # diccionario completo del libro encontrado,
            # extraído de "libros" usando la posición "pos".
            libro = libros[pos]

            # "estado" (variable GLOBAL en este bloque): texto
            # "DISPONIBLE" o "SIN COPIAS" para mostrar al
            # usuario, calculado igual que en mostrar_libros.
            estado = "DISPONIBLE" if libro["disponible"] else "SIN COPIAS"
            print(f"\nLibro encontrado en la posición {pos}:")
            print(f"Título: {libro['titulo']} | Copias: {libro['copias']} | Préstamo: {libro['prestamo']} días | Estado: {estado}\n")
        else:
            print("Libro no encontrado.")

    elif opcion == 3:
        eliminar_libro(libros)

    elif opcion == 4:
        actualizar_disponibilidad(libros)
        print("Disponibilidad actualizada.")

    elif opcion == 5:
        mostrar_libros(libros)

    elif opcion == 6:
        print("Gracias por usar el sistema. Vuelva pronto.")
    
        break #Se termina el bucle principal y con ello el programa completo.

