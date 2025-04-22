# Documentación Básica de Python para Principiantes

> Esta documentación está diseñada para quienes están comenzando en el mundo del desarrollo con Python. Se encuentra en formato **Markdown**, un lenguaje ligero de marcado ideal para la creación de documentación técnica. Puedes visualizar este documento en plataformas como GitHub, Visual Studio Code o cualquier editor Markdown.

---

## ¿Qué es un condicional?

Un **condicional** permite que el programa tome decisiones en función de si una condición se cumple o no. En Python, los condicionales más comunes son `if`, `elif` y `else`.

### Sintaxis
```python
if condicion:
    # código si la condición es verdadera
elif otra_condicion:
    # código si la otra condición es verdadera
else:
    # código si ninguna condición se cumplió
```

### Ejemplo
```python
edad = 18

if edad >= 18:
    print("Eres mayor de edad")
elif edad == 17:
    print("Casi eres mayor de edad")
else:
    print("Eres menor de edad")
```

---

## ¿Cuáles son los diferentes tipos de bucles en Python? ¿Por qué son útiles?

### Tipos de bucles

1. **Bucle `for`**: Se usa para iterar sobre una secuencia (lista, tupla, cadena, etc).
```python
for i in range(5):
    print(i)
```

2. **Bucle `while`**: Repite un bloque de código mientras una condición sea verdadera.
```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

### ¿Por qué son útiles?
Los bucles nos permiten **automatizar tareas repetitivas**, recorrer estructuras de datos, ejecutar procesos de forma controlada y eficiente.

---

## ¿Qué es una lista por comprensión en Python?

Es una forma concisa de crear listas utilizando una sola línea de código. Es más legible y eficiente que usar bucles `for` convencionales.

### Sintaxis
```python
[nueva_expresion for item in iterable if condicion]
```

### Ejemplo
```python
cuadrados = [x**2 for x in range(10) if x % 2 == 0]
print(cuadrados)  # Salida: [0, 4, 16, 36, 64]
```

---

## ¿Qué es un argumento en Python?

Los **argumentos** son valores que se pasan a una función cuando esta es llamada. Permiten personalizar el comportamiento de la función.

### Tipos de argumentos:
1. **Posicionales**:
```python
def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Ana")
```

2. **Por defecto**:
```python
def saludar(nombre="amigo"):
    print(f"Hola, {nombre}!")

saludar()  # Hola, amigo!
```

3. **Arbitrarios**:
```python
def sumar(*args):
    print(sum(args))

sumar(1, 2, 3)
```

---

## ¿Qué es una función Lambda en Python?

Una **función lambda** es una función anónima (sin nombre) definida en una sola línea. Se usa para operaciones simples y rápidas.

### Sintaxis
```python
lambda argumentos: expresion
```

### Ejemplo
```python
doblar = lambda x: x * 2
print(doblar(5))  # Salida: 10
```

### Uso común
Se usa mucho con funciones como `map()`, `filter()` o `sorted()`:
```python
numeros = [1, 2, 3, 4]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4]
```

---

## ¿Qué es un paquete pip?

`pip` es el **gestor de paquetes de Python**. Permite instalar librerías y paquetes de terceros que no vienen incluidos por defecto con Python.

### Comandos básicos
- **Instalar un paquete:**
```bash
pip install nombre_del_paquete
```
- **Actualizar un paquete:**
```bash
pip install --upgrade nombre_del_paquete
```
- **Ver paquetes instalados:**
```bash
pip list
```

### Ejemplo
```bash
pip install requests
```
```python
import requests
respuesta = requests.get("https://api.github.com")
print(respuesta.status_code)
```

---

## Recomendaciones de herramientas para documentación

- **Visual Studio Code** (con extensiones Markdown Preview)
- **Typora** (editor visual de Markdown)
- **Docusaurus** o **MkDocs** (para documentación en sitios web)
- **GitHub** (ideal para publicar y versionar tu documentación)

---

## Recursos adicionales

- [Documentación oficial de Python](https://docs.python.org/es/3/)
- [Tutorial interactivo de Python](https://www.learnpython.org/)
- [Cheat Sheet de Markdown](https://www.markdownguide.org/cheat-sheet/)

