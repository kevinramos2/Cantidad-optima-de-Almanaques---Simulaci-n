#Código hecho por Kevin Ramos
import math as m
import random as ran
import numpy as np

def ventas():
  #Esta función me genera un numero aleatorio entre 0 y 1
  acum = ran.random()
  #Se comprueba usando la función uniforme acumulada, esta nos retorna el número de almanaques que se venden
  if acum <= 0.3:
    resultado = 100
  elif acum <= 0.5:
    resultado = 150
  elif acum <= 0.8:
    resultado = 200
  elif acum <= 0.95:
    resultado = 250
  elif acum <= 1:
    resultado = 300
  #Se retorna el total de almanaques que se venden
  return resultado

#Función para calcular el número de simulaciones adecuadas
def calcularN(sd, D=10):
  z = 1.96  # Valor z para 95% de confianza
  n = ((z**2) * (sd**2)) / (D**2)
  return int(n)

#Función para obtener la desviación de una Muestra de 10000
def simulacionParaDesv(encargo):
  #Lista donde se almancenarán las ganancias en cada simulación
  ganancias = []
  #Ciclo que se itera 10 mil veces
  for i in range(10000):
    #Hallamos un r entre 0 y 1
    r = ran.random()
    #Usamos la transformada inversa para hallar x (costo por unidad)
    x = ((2-(1.5))*r) + 1.5
    #Calculamos costo total
    costo = x*encargo
    #Obtenemos el número de ventas
    almanaquesVendidos = ventas()
    #Verificamos que la demanda esté acorde a la oferta
    while almanaquesVendidos > encargo:
      almanaquesVendidos = ventas()
    #El total de las ventas
    totalVenta = almanaquesVendidos*4.5
    #Calculamos la utilidad
    utilidad = ((totalVenta-costo)+((encargo-almanaquesVendidos)*0.75))
    #añadimos cada utilidad a la lista de ganancias
    ganancias.append(utilidad)

  #Calculamos la desviación estándar de una muestra de 10 mil simulaciones
  desviacionS = np.std(ganancias)
  return  desviacionS

#Función para obtener las ganancias óptimas al comprar X cantidad almanaques
def simulacionCompleto(N,encargo):
  #Lista donde se almancenarán las ganancias en cada simulación
  ganancias = []
  #Ciclo que se N veces
  for i in range(N):
    #Hallamos un r entre 0 y 1
    r = ran.random()
    #Usamos la transformada inversa para hallar x (costo por unidad)
    x = ((2-(1.5))*r) + 1.5
    #Calculamos costo total
    costo = x*encargo
    #Obtenemos el número de ventas
    almanaquesVendidos = ventas()
    #Verificamos que la demanda esté acorde a la oferta
    while almanaquesVendidos > encargo:
      almanaquesVendidos = ventas()

    #El total de las ventas
    totalVenta = almanaquesVendidos*4.5
    #Calculamos la utilidad
    utilidad = ((totalVenta-costo)+((encargo-almanaquesVendidos)*0.75))
    #añadimos cada utilidad a la lista de ganancias
    ganancias.append(utilidad)

  #Definimos los datos estadísticos fijándonos en la lista de ganancias
  mediaGanancias = np.mean(ganancias)
  desvGanancias = np.std(ganancias)
  minGanancia = min(ganancias)
  maxGanancia = max(ganancias)

  # Cálculo del intervalo de confianza del 95%
  Z = 1.96  # valor z para 95% de confianza
  margenError = Z * (desvGanancias / m.sqrt(N))
  ic_inferior = mediaGanancias - margenError
  ic_superior = mediaGanancias + margenError

  return {
         "Media de ganancias: ":mediaGanancias,
         "Desviación estándar de las ganancias: ":desvGanancias,
         "Ganancia mínima: ":minGanancia,
         "Ganancia máxima: ":maxGanancia,
         "IC 95% Inferior: ": ic_inferior,
         "IC 95% Superior: ": ic_superior
        }

#Para 100 almanaques
ds100 = simulacionParaDesv(100)
sim100 = calcularN(ds100)
print("La desviación estándar cuando se encargan 100 almanaques en una muestra de 10000 es: ",ds100)
print("El número indicado de simulaciones es: ", sim100)
todo100 = simulacionCompleto(sim100,100)
print()
print("--- Resultados para 100 almanaques ---")
for key, value in todo100.items():
    print(f"{key} {value}")
print()

#Para 150 almanaques
ds150 = simulacionParaDesv(150)
sim150 = calcularN(ds150)
print("La desviación estándar cuando se encargan 150 almanaques en una muestra de 10000 es: ",ds150)
print("El número indicado de simulaciones es: ", sim150)
todo150 = simulacionCompleto(sim150,150)
print()
print("--- Resultados para 150 almanaques ---")
for key, value in todo150.items():
    print(f"{key} {value}")
print()

#Para 200 almanaques
ds200 = simulacionParaDesv(200)
sim200 = calcularN(ds200)
print("La desviación estándar cuando se encargan 200 almanaques en una muestra de 10000 es: ",ds200)
print("El número indicado de simulaciones es: ", sim200)
todo200 = simulacionCompleto(sim200,200)
print()
print("--- Resultados para 200 almanaques ---")
for key, value in todo200.items():
    print(f"{key} {value}")
print()

#Para 250 almanaques
ds250 = simulacionParaDesv(250)
sim250 = calcularN(ds250)
print("La desviación estándar cuando se encargan 250 almanaques en una muestra de 10000 es: ",ds250)
print("El número indicado de simulaciones es: ", sim250)
todo250 = simulacionCompleto(sim250,250)
print()
print("--- Resultados para 250 almanaques ---")
for key, value in todo250.items():
    print(f"{key} {value}")
print()

#Para 300 almanaques
ds300 = simulacionParaDesv(300)
sim300 = calcularN(ds300)
print("La desviación estándar cuando se encargan 300 almanaques en una muestra de 10000 es: ",ds300)
print("El número indicado de simulaciones es: ", sim300)
todo300 = simulacionCompleto(sim300,300)
print()
print("--- Resultados para 300 almanaques ---")
for key, value in todo300.items():
    print(f"{key} {value}")
print()

