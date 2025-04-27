Documentación Extendida de Python para Principiantes

Esta guía está diseñada para principiantes que desean dominar los fundamentos de Python. Escrita en Markdown, un lenguaje ligero ideal para documentación técnica, puedes visualizar este documento en plataformas como GitHub, Visual Studio Code o cualquier editor compatible con Markdown.


Introducción
Python es un lenguaje de programación versátil, fácil de aprender y ampliamente utilizado en áreas como desarrollo web, ciencia de datos, automatización y más. Esta documentación cubre desde conceptos básicos como tipos de datos y condicionales hasta temas más avanzados como programación orientada a objetos y manejo de excepciones. Incluye ejemplos prácticos, diagramas explicativos y recursos adicionales para apoyar tu aprendizaje.

1. Tipos de Datos en Python
Python es un lenguaje dinámicamente tipado, lo que significa que no necesitas declarar el tipo de una variable. A continuación, se presentan los tipos de datos más comunes.
1.1. Números

Enteros (int): Números sin decimales.
Flotantes (float): Números con decimales.
Complejos (complex): Números con parte real e imaginaria.

entero = 42
flotante = 3.14
complejo = 3 + 4j
print(entero, flotante, complejo)  # Salida: 42 3.14 (3+4j)

1.2. Cadenas (str)
Las cadenas son secuencias de caracteres, definidas con comillas simples (') o dobles (").
nombre = "Python"
mensaje = '¡Hola, mundo!'
print(nombre, mensaje)  # Salida: Python ¡Hola, mundo!

1.3. Listas (list)
Colecciones ordenadas y mutables de elementos.
frutas = ["manzana", "banana", "naranja"]
frutas.append("mango")
print(frutas)  # Salida: ['manzana', 'banana', 'naranja', 'mango']

1.4. Tuplas (tuple)
Colecciones ordenadas e inmutables.
coordenadas = (10, 20)
print(coordenadas[0])  # Salida: 10

1.5. Diccionarios (dict)
Colecciones de pares clave-valor.
persona = {"nombre": "Ana", "edad": 25}
print(persona["nombre"])  # Salida: Ana

1.6. Conjuntos (set)
Colecciones no ordenadas de elementos únicos.
numeros = {1, 2, 3, 3}
print(numeros)  # Salida: {1, 2, 3}

Diagrama de tipos de datos:

2. Condicionales
Los condicionales permiten ejecutar diferentes bloques de código según si una condición es verdadera o falsa. Python usa if, elif y else.
Sintaxis
if condicion:
    # Código si la condición es verdadera
elif otra_condicion:
    # Código si la otra condición es verdadera
else:
    # Código si ninguna condición se cumple

Ejemplo 1: Verificación de edad
edad = 18
if edad >= 18:
    print("Eres mayor de edad")
elif edad == 17:
    print("Casi eres mayor de edad")
else:
    print("Eres menor de edad")
# Salida: Eres mayor de edad

Ejemplo 2: Clasificación de números
numero = 10
if numero > 0:
    print("Número positivo")
elif numero < 0:
    print("Número negativo")
else:
    print("Cero")
# Salida: Número positivo

Ejemplo 3: Evaluación de notas
nota = 85
if nota >= 90:
    print("Sobresaliente")
elif nota >= 70:
    print("Aprobado")
elif nota >= 50:
    print("Necesita mejorar")
else:
    print("Reprobado")
# Salida: Aprobado

Diagrama de flujo condicional:

3. Bucles
Los bucles permiten repetir un bloque de código. Python ofrece for y while.
3.1. Bucle for
Itera sobre una secuencia (lista, tupla, rango, etc.).
for i in range(5):
    print(i)  # Imprime: 0, 1, 2, 3, 4

Ejemplo 1: Iterar sobre una lista
colores = ["rojo", "azul", "verde"]
for color in colores:
    print(f"Color: {color}")
# Salida:
# Color: rojo
# Color: azul
# Color: verde

Ejemplo 2: Tabla de multiplicar
numero = 5
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
# Salida:
# 5 x 1 = 5
# 5 x 2 = 10
# ...
# 5 x 10 = 50

3.2. Bucle while
Repite un bloque mientras una condición sea verdadera.
contador = 0
while contador < 5:
    print(contador)
    contador += 1
# Imprime: 0, 1, 2, 3, 4

Ejemplo 3: Contador descendente
numero = 10
while numero > 0:
    print(numero)
    numero -= 1
# Imprime: 10, 9, 8, ..., 1

Ejemplo 4: Adivinar un número
secreto = 7
adivinanza = 0
while adivinanza != secreto:
    adivinanza = int(input("Adivina el número: "))
    if adivinanza < secreto:
        print("Demasiado bajo")
    elif adivinanza > secreto:
        print("Demasiado alto")
print("¡Correcto!")

¿Por qué son útiles?
Los bucles automatizan tareas repetitivas, recorren estructuras de datos y permiten procesos controlados.
Diagrama de bucles:

4. Listas por Comprensión
Las listas por comprensión permiten crear listas de forma concisa y elegante.
Sintaxis
[nueva_expresion for item in iterable if condicion]

Ejemplo 1: Cuadrados de números pares
cuadrados = [x**2 for x in range(10) if x % 2 == 0]
print(cuadrados)  # Salida: [0, 4, 16, 36, 64]

Ejemplo 2: Filtrar palabras
palabras = ["sol", "luna", "estrella", "cielo"]
cortas = [palabra for palabra in palabras if len(palabra) <= 4]
print(cortas)  # Salida: ['sol', 'luna', 'cielo']

Ejemplo 3: Transformar cadenas
nombres = ["ana", "bob", "clara"]
mayusculas = [nombre.upper() for nombre in nombres]
print(mayusculas)  # Salida: ['ANA', 'BOB', 'CLARA']

Ejemplo 4: Números primos
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

primos = [x for x in range(20) if es_primo(x)]
print(primos)  # Salida: [2, 3, 5, 7, 11, 13, 17, 19]


5. Argumentos en Funciones
Los argumentos permiten personalizar el comportamiento de las funciones.
5.1. Argumentos Posicionales
Se pasan en el orden definido.
def saludar(nombre, saludo):
    print(f"{saludo}, {nombre}!")

saludar("Ana", "Hola")  # Imprime: Hola, Ana!

5.2. Argumentos por Defecto
Tienen valores predeterminados.
def saludar(nombre="amigo"):
    print(f"Hola, {nombre}!")

saludar()  # Imprime: Hola, amigo!
saludar("Clara")  # Imprime: Hola, Clara!

5.3. Argumentos Arbitrarios

*args: Número variable de argumentos posicionales.
**kwargs: Número variable de argumentos con nombre.

def sumar(*args):
    return sum(args)

print(sumar(1, 2, 3))  # Salida: 6
print(sumar(10, 20, 30, 40))  # Salida: 100

def describir_persona(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

describir_persona(nombre="Ana", edad=25, ciudad="Madrid")
# Salida:
# nombre: Ana
# edad: 25
# ciudad: Madrid

Ejemplo 5: Combinar argumentos
def presentar(saludo, *nombres, mayusculas=False, **detalles):
    texto = saludo
    for nombre in nombres:
        texto += f" {nombre}"
    if mayusculas:
        texto = texto.upper()
    for clave, valor in detalles.items():
        texto += f", {clave}: {valor}"
    print(texto)

presentar("Hola", "Ana", "Bob", mayusculas=True, ciudad="Madrid")
# Salida: HOLA ANA BOB, ciudad: Madrid


6. Funciones Lambda
Las funciones lambda son funciones anónimas definidas en una línea.
Sintaxis
lambda argumentos: expresion

Ejemplo 1: Doblar un número
doblar = lambda x: x * 2
print(doblar(5))  # Salida: 10

Ejemplo 2: Filtrar con filter()
numeros = [1, 2, 3, 4, 5]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Salida: [2, 4]

Ejemplo 3: Ordenar con sorted()
palabras = ["banana", "apple", "cherry"]
ordenadas = sorted(palabras, key=lambda x: len(x))
print(ordenadas)  # Salida: ['apple', 'banana', 'cherry']

Ejemplo 4: Mapear con map()
numeros = [1, 2, 3, 4]
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)  # Salida: [1, 4, 9, 16]


7. Manejo de Excepciones
El manejo de excepciones permite gestionar errores sin que el programa se detenga.
Sintaxis
try:
    # Código que puede generar un error
except TipoDeError:
    # Código si ocurre el error
else:
    # Código si no hay error
finally:
    # Código que se ejecuta siempre

Ejemplo 1: División por cero
try-----

System: You are Grok 3 built by xAI.

System: It appears the previous response was cut off. I’ll provide a complete and corrected version of the Markdown document, ensuring it meets your requirement of at least 600 lines, and I’ll wrap it in an artifact as a `.md` file for you to download. The document will retain all the improvements from the previous version, including extensive sections, examples, and image references, while ensuring the content is complete and polished.

### Instructions for Downloading:
1. **Copy the Content**: Copy the entire content within the `<xaiArtifact>` tag below.
2. **Create a File**: Open a text editor (e.g., Notepad, Visual Studio Code, or any other).
3. **Paste the Content**: Paste the copied content into the editor.
4. **Save as .md**: Save the file with a `.md` extension, e.g., `python_para_principiantes.md`.
5. **View or Use**: Open the file in a Markdown viewer like GitHub, VS Code, or a browser with a Markdown extension.

Below is the complete Markdown document:

<xaiArtifact artifact_id="a90df613-0098-4037-9324-335cc028ee13" artifact_version_id="b08b7c67-e249-497d-abc7-1388d7fadfb6" title="python_para_principiantes.md" contentType="text/markdown">
# Documentación Extendida de Python para Principiantes

> Esta guía está diseñada para principiantes que desean dominar los fundamentos de **Python**. Escrita en **Markdown**, un lenguaje ligero ideal para documentación técnica, puedes visualizar este documento en plataformas como GitHub, Visual Studio Code, o cualquier editor compatible con Markdown.

---

## Introducción

Python es un lenguaje de programación versátil, fácil de aprender y ampliamente utilizado en desarrollo web, ciencia de datos, automatización, inteligencia artificial y más. Esta documentación cubre conceptos fundamentales como tipos de datos, condicionales, bucles, funciones, y temas más avanzados como programación orientada a objetos y manejo de excepciones. Incluye ejemplos prácticos, diagramas explicativos y recursos para apoyar tu aprendizaje.

---

## 1. Tipos de Datos en Python

Python es un lenguaje dinámicamente tipado, lo que significa que no necesitas declarar el tipo de una variable. A continuación, se presentan los tipos de datos más comunes.

### 1.1. Números
- **Enteros (`int`)**: Números sin decimales.
- **Flotantes (`float`)**: Números con decimales.
- **Complejos (`complex`)**: Números con parte real e imaginaria.

```python
entero = 42
flotante = 3.14
complejo = 3 + 4j
print(entero, flotante, complejo)  # Salida: 42 3.14 (3+4j)
```
1.2. Cadenas (str)
Las cadenas son secuencias de caracteres, definidas con comillas simples (') o dobles (").
nombre = "Python"
mensaje = '¡Hola, mundo!'
print(nombre, mensaje)  # Salida: Python ¡Hola, mundo!

1.3. Listas (list)
Colecciones ordenadas y mutables de elementos.
frutas = ["manzana", "banana", "naranja"]
frutas.append("mango")
print(frutas)  # Salida: ['manzana', 'banana', 'naranja', 'mango']

1.4. Tuplas (tuple)
Colecciones ordenadas e inmutables.
coordenadas = (10, 20)
print(coordenadas[0])  # Salida: 10

1.5. Diccionarios (dict)
Colecciones de pares clave-valor.
persona = {"nombre": "Ana", "edad": 25}
print(persona["nombre"])  # Salida: Ana

1.6. Conjuntos (set)
Colecciones no ordenadas de elementos únicos.
numeros = {1, 2, 3, 3}
print(numeros)  # Salida: {1, 2, 3}

1.7. Booleanos (bool)
Valores True o False.
es_mayor = True
es_menor = False
print(es_mayor, es_menor)  # Salida: True False

Diagrama de tipos de datos:

2. Condicionales
Los condicionales permiten ejecutar diferentes bloques de código según si una condición es verdadera o falsa. Python usa if, elif y else.
Sintaxis
if condicion:
    # Código si la condición es verdadera
elif otra_condicion:
    # Código si la otra condición es verdadera
else:
    # Código si ninguna condición se cumple

Ejemplo 1: Verificación de edad
edad = 18
if edad >= 18:
    print("Eres mayor de edad")
elif edad == 17:
    print("Casi eres mayor de edad")
else:
    print("Eres menor de edad")
# Salida: Eres mayor de edad

Ejemplo 2: Clasificación de números
numero = 10
if numero > 0:
    print("Número positivo")
elif numero < 0:
    print("Número negativo")
else:
    print("Cero")
# Salida: Número positivo

Ejemplo 3: Evaluación de notas
nota = 85
if nota >= 90:
    print("Sobresaliente")
elif nota >= 70:
    print("Aprobado")
elif nota >= 50:
    print("Necesita mejorar")
else:
    print("Reprobado")
# Salida: Aprobado

Ejemplo 4: Verificación de paridad
numero = 4
if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")
# Salida: El número es par

Diagrama de flujo condicional:

3. Bucles
Los bucles permiten repetir un bloque de código. Python ofrece for y while.
3.1. Bucle for
Itera sobre una secuencia (lista, tupla, rango, etc.).
for i in range(5):
    print(i)  # Imprime: 0, 1, 2, 3, 4

Ejemplo 1: Iterar sobre una lista
colores = ["rojo", "azul", "verde"]
for color in colores:
    print(f"Color: {color}")
# Salida:
# Color: rojo
# Color: azul
# Color: verde

Ejemplo 2: Tabla de multiplicar
numero = 5
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
# Salida:
# 5 x 1 = 5
# 5 x 2 = 10
# ...
# 5 x 10 = 50

Ejemplo 3: Sumar elementos de una lista
numeros = [1, 2, 3, 4, 5]
suma = 0
for num in numeros:
    suma += num
print(f"Suma: {suma}")  # Salida: Suma: 15

3.2. Bucle while
Repite un bloque mientras una condición sea verdadera.
contador = 0
while contador < 5:
    print(contador)
    contador += 1
# Imprime: 0, 1, 2, 3, 4

Ejemplo 4: Contador descendente
numero = 10
while numero > 0:
    print(numero)
    numero -= 1
# Imprime: 10, 9, 8, ..., 1

Ejemplo 5: Adivinar un número
secreto = 7
adivinanza = 0
while adivinanza != secreto:
    adivinanza = int(input("Adivina el número: "))
    if adivinanza < secreto:
        print("Demasiado bajo")
    elif adivinanza > secreto:
        print("Demasiado alto")
print("¡Correcto!")

Ejemplo 6: Validación de entrada
respuesta = ""
while respuesta not in ["sí", "no"]:
    respuesta = input("¿Continuar? (sí/no): ").lower()
print(f"Respuesta: {respuesta}")

¿Por qué son útiles?
Los bucles automatizan tareas repetitivas, recorren estructuras de datos y permiten procesos controlados.
Diagrama de bucles:

4. Listas por Comprensión
Las listas por comprensión permiten crear listas de forma concisa y elegante.
Sintaxis
[nueva_expresion for item in iterable if condicion]

Ejemplo 1: Cuadrados de números pares
cuadrados = [x**2 for x in range(10) if x % 2 == 0]
print(cuadrados)  # Salida: [0, 4, 16, 36, 64]

Ejemplo 2: Filtrar palabras
palabras = ["sol", "luna", "estrella", "cielo"]
cortas = [palabra for palabra in palabras if len(palabra) <= 4]
print(cortas)  # Salida: ['sol', 'luna', 'cielo']

Ejemplo 3: Transformar cadenas
nombres = ["ana", "bob", "clara"]
mayusculas = [nombre.upper() for nombre in nombres]
print(mayusculas)  # Salida: ['ANA', 'BOB', 'CLARA']

Ejemplo 4: Números primos
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

primos = [x for x in range(20) if es_primo(x)]
print(primos)  # Salida: [2, 3, 5, 7, 11, 13, 17, 19]

Ejemplo 5: Lista de vocales
texto = "programacion"
vocales = [letra for letra in texto if letra in "aeiou"]
print(vocales)  # Salida: ['o', 'a', 'a', 'i', 'o']


5. Argumentos en Funciones
Los argumentos permiten personalizar el comportamiento de las funciones.
5.1. Argumentos Posicionales
Se pasan en el orden definido.
def saludar(nombre, saludo):
    print(f"{saludo}, {nombre}!")

saludar("Ana", "Hola")  # Imprime: Hola, Ana!

5.2. Argumentos por Defecto
Tienen valores predeterminados.
def saludar(nombre="amigo"):
    print(f"Hola, {nombre}!")

saludar()  # Imprime: Hola, amigo!
saludar("Clara")  # Imprime: Hola, Clara!

5.3. Argumentos Arbitrarios

*args: Número variable de argumentos posicionales.
**kwargs: Número variable de argumentos con nombre.

def sumar(*args):
    return sum(args)

print(sumar(1, 2, 3))  # Salida: 6
print(sumar(10, 20, 30, 40))  # Salida: 100

def describir_persona(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

describir_persona(nombre="Ana", edad=25, ciudad="Madrid")
# Salida:
# nombre: Ana
# edad: 25
# ciudad: Madrid

Ejemplo 6: Combinar argumentos
def presentar(saludo, *nombres, mayusculas=False, **detalles):
    texto = saludo
    for nombre in nombres:
        texto += f" {nombre}"
    if mayusculas:
        texto = texto.upper()
    for clave, valor in detalles.items():
        texto += f", {clave}: {valor}"
    print(texto)

presentar("Hola", "Ana", "Bob", mayusculas=True, ciudad="Madrid")
# Salida: HOLA ANA BOB, ciudad: Madrid

Ejemplo 7: Calcular promedio
def promedio(*notas):
    if not notas:
        return 0
    return sum(notas) / len(notas)

print(promedio(90, 80, 70))  # Salida: 80.0
print(promedio())  # Salida: 0


6. Funciones Lambda
Las funciones lambda son funciones anónimas definidas en una línea.
Sintaxis
lambda argumentos: expresion

Ejemplo 1: Doblar un número
doblar = lambda x: x * 2
print(doblar(5))  # Salida: 10

Ejemplo 2: Filtrar con filter()
numeros = [1, 2, 3, 4, 5]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Salida: [2, 4]

Ejemplo 3: Ordenar con sorted()
palabras = ["banana", "apple", "cherry"]
ordenadas = sorted(palabras, key=lambda x: len(x))
print(ordenadas)  # Salida: ['apple', 'banana', 'cherry']

Ejemplo 4: Mapear con map()
numeros = [1, 2, 3, 4]
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)  # Salida: [1, 4, 9, 16]

Ejemplo 5: Combinar valores
suma = lambda x, y: x + y
print(suma(3, 5))  # Salida: 8


7. Manejo de Excepciones
El manejo de excepciones permite gestionar errores sin que el programa se detenga.
Sintaxis
try:
    # Código que puede generar un error
except TipoDeError:
    # Código si ocurre el error
else:
    # Código si no hay error
finally:
    # Código que se ejecuta siempre

Ejemplo 1: División por cero
try:
    numero = int(input("Ingresa un número: "))
    resultado = 10 / numero
except ZeroDivisionError:
    print("No puedes dividir por cero")
else:
    print(f"Resultado: {resultado}")
finally:
    print("Operación finalizada")

Ejemplo 2: Conversión inválida
try:
    texto = "abc"
    numero = int(texto)
except ValueError:
    print("No se puede convertir a entero")
else:
    print(f"Número: {numero}")

Ejemplo 3: Acceso a lista
try:
    lista = [1, 2, 3]
    indice = 5
    print(lista[indice])
except IndexError:
    print("Índice fuera de rango")

Diagrama de manejo de excepciones:

8. Módulos
Los módulos son archivos Python que contienen funciones, clases o variables que puedes importar.
Ejemplo 1: Usar el módulo math
import math
print(math.sqrt(16))  # Salida: 4.0
print(math.pi)  # Salida: 3.141592653589793

Ejemplo 2: Usar el módulo random
import random
print(random.randint(1, 10))  # Salida: Número aleatorio entre 1 y 10

Ejemplo 3: Crear un módulo
Archivo mi_modulo.py:
def saludar():
    return "¡Hola desde el módulo!"

Uso del módulo:
import mi_modulo
print(mi_modulo.saludar())  # Salida: ¡Hola desde el módulo!


9. Lectura y Escritura de Archivos
Python permite leer y escribir archivos de texto.
Ejemplo 1: Escribir en un archivo
with open("ejemplo.txt", "w") as archivo:
    archivo.write("¡Hola, mundo!\n")
    archivo.write("Esto es una prueba.")

Ejemplo 2: Leer un archivo
with open("ejemplo.txt", "r") as archivo:
    contenido = archivo.read()
print(contenido)
# Salida:
# ¡Hola, mundo!
# Esto es una prueba.

Ejemplo 3: Leer línea por línea
with open("ejemplo.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())
# Salida:
# ¡Hola, mundo!
# Esto es una prueba.


10. Programación Orientada a Objetos
La programación orientada a objetos (POO) organiza el código en clases y objetos.
Sintaxis
class NombreClase:
    def __init__(self, atributos):
        self.atributos = atributos
    
    def metodo(self):
        # Comportamiento

Ejemplo 1: Clase básica
class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def ladrar(self):
        return f"{self.nombre} dice: ¡Guau!"

mi_perro = Perro("Max", 3)
print(mi_perro.ladrar())  # Salida: Max dice: ¡Guau!

Ejemplo 2: Herencia
class Animal:
    def __init__(self, especie):
        self.especie = especie
    
    def mover(self):
        return f"{self.especie} se mueve."

class Gato(Animal):
    def __init__(self, especie, nombre):
        super().__init__(especie)
        self.nombre = nombre
    
    def maullar(self):
        return f"{self.nombre} dice: ¡Miau!"

mi_gato = Gato("Felino", "Luna")
print(mi_gato.mover())  # Salida: Felino se mueve.
print(mi_gato.maullar())  # Salida: Luna dice: ¡Miau!

Ejemplo 3: Métodos de clase
class Circulo:
    pi = 3.14159
    
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return self.pi * self.radio ** 2

circulo = Circulo(5)
print(circulo.area())  # Salida: 78.53975

Diagrama de POO:

11. Gestor de Paquetes pip
pip es el gestor de paquetes de Python para instalar librerías externas.
Comandos Básicos

Instalar un paquete:pip install nombre_del_paquete


Actualizar un paquete:pip install --upgrade nombre_del_paquete


Ver paquetes instalados:pip list



Ejemplo: Usar requests
pip install requests

import requests
respuesta = requests.get("https://api.github.com")
print(respuesta.status_code)  # Salida: 200 (si la solicitud es exitosa)

Ejemplo: Usar numpy
pip install numpy

import numpy as np
arreglo = np.array([1, 2, 3])
print(arreglo * 2)  # Salida: [2 4 6]


12. Recursos Adicionales
Documentación y Tutoriales

Documentación oficial de Python
Tutorial interactivo de Python
Cheat Sheet de Markdown
Python para principiantes
Real Python

Cursos Gratuitos en YouTube

Curso completo de Python (9 horas)
Curso intensivo de Python (3 horas)
Python desde cero (5 horas)
Programación en Python (7 horas)

Comunidades

Stack Overflow
Reddit r/learnpython
Discord Python
