for i in range(5):    
    print(i)

def suma (a, b, c):
  return a + b + c

resultado= suma(15, 20, 30)
print(resultado)

suma =lambda a, b, c: a + b + c
resultado= suma(15, 20, 30)
print(resultado)

nombre = 'Enrique'
lista_nombre = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'

encontrado = False
for n in lista_nombre:
    if n == nombre:
        encontrado = True
        break
        
if encontrado:
    print('el nombre se encontró')
else:
    print('No se encontró el nombre')
   