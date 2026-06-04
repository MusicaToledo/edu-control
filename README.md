# Edu-Control 🏫📚
Proyecto que armado para la asignatura Estructura de datos y algortimos. Es un sistema básico, hecho completamente en Python, que funciona por consola y sirve para gestionar tareas típicas de un colegio. 

## ¿Qué se puede hacer hasta ahora?
El sistema se centra en administrar a los estudiantes y tiene estas funciones principales:
* **Gestión de contraseñas:** Los alumnos pueden crear su clave por primera vez o cambiarla si ya tienen una (el sistema valida que las claves coincidan y no estén en blanco).
* **Fichas Académicas:** Permite buscar a un alumno usando su RUT para ver toda su información y registro en pantalla.
* **Certificados de Matrícula:** Genera e imprime un certificado básico indicando el nombre y el curso del estudiante (pide validar la contraseña antes de mostrarlo).

## Herramientas utilizadas
* **Lenguaje:** Python 🐍.

## 🧩 Estructura del Código (Clases y Funciones)

### 👨‍🎓 Clase `Alumno` (en `alumno.py`)
* `__init__(self, rut, nombre, apellido, curso)`: El constructor. Al registrar un alumno nuevo, le asigno estos datos básicos y dejo su contraseña como `None` (vacía) al principio.
* `creacion_de_clave(self, clave)`: Toma la contraseña que escribe el usuario y se la guarda al objeto del alumno. 
* `validar_clave(self, clave)`: Compara la clave que ingresa el usuario en la consola con la que el alumno tiene guardada. Retorna `True` si se valida o `False` si se equivoca.
* `ficha_alumno(self)`: Imprime en pantalla los datos personales y el curso del estudiante de forma ordenada.
* `obtener_certificado(self)`: Imprime en pantalla los datos personales y el curso del estudiante de forma ordenada.

### 🏫 Clase `Colegio` (en `colegio.py`)
* `__init__(self)`: Es el constructor de la clase. Al iniciar, crea automáticamente un registro global con los 12 cursos predefinidos (desde 1ro Básico hasta 4to Medio), dejándolos listos para recibir alumnos.
* `agregar_alumno(self, alumno)`: Recibe el objeto de un estudiante recién creado y lo guarda directamente en el diccionario del curso que le corresponde.
* `obtener_registro_global(self)`: Devuelve el "libro de clases" completo, es decir, el diccionario con todos los cursos y los alumnos que se han registrado en el sistema.
* `obtener_cursos(self)`: Entrega una lista limpia solo con los nombres de los cursos disponibles para poder mostrarlos fácilmente en los menús.
* `buscar_alumno_por_rut(self, rut)`: Funciona como un buscador. Recorre todos los cursos revisando si hay algún alumno matriculado con el RUT solicitado y devuelve su información si lo encuentra.

### 👨‍💼 Clase `Administrador` (en `administrador.py`)
Esta clase es súper cortita pero fundamental. Actúa como el guardia de seguridad para proteger el acceso al menú del colegio.

* `__init__(self)`: Es el constructor. Al iniciar, simplemente guarda la clave maestra o secreta del sistema (que por ahora está fijada como "Edu2026").
* `validar_clave(self, clave)`: Toma la contraseña que alguien escribe intentando entrar como administrador y la compara con la clave maestra guardada. Si son exactamente iguales, te da luz verde (`True`), y si no, te bloquea el paso (`False`).

### ⚙️ Funciones Principales (en `main.py`)
* **panel_principal():** Es el menú de inicio y el motor del programa. Te pregunta si quieres entrar como Administrador, como Alumno o si prefieres salir del sistema.
* **validacion_clave(usuario, rol):** Es el sistema de seguridad. Te da 3 intentos para ingresar tu contraseña correctamente; si fallas, te bloquea el acceso y te devuelve al menú.
* **panel_admin():** El menú exclusivo del colegio. Desde aquí el administrador puede registrar nuevos estudiantes o buscar las fichas de los que ya están matriculados.
* **registrar_alumno():** Se encarga de pedir los datos (RUT, nombre, apellido y curso), valida que no haya errores (como RUTs repetidos o campos vacíos) y guarda al nuevo alumno en el sistema.
* **panel_alumno():** El menú de los estudiantes. Pide tu RUT y clave para iniciar sesión y te da las opciones para ver tu ficha, sacar tu certificado o cambiar tu contraseña.
* **gestionar_clave_alumno(alumno):** Administra las contraseñas: si es tu primera vez, te obliga a crear una; si ya tienes, te pide la actual por seguridad antes de dejarte modificarla.
* **obtener_ficha(alumno):** Muestra el registro académico en pantalla. Si el administrador la usa, pide ingresar el RUT por teclado para buscar al alumno antes de mostrar los datos.
* **generar_certificado(alumno):** Imprime un "Certificado de Matrícula" formal en la consola, pero exige que ingreses tu clave nuevamente por seguridad antes de dejarte verlo.
