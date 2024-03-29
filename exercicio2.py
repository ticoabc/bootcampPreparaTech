# -*- coding: utf-8 -*-
"""exercicio2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Wl-wL_vUtKHPHl_v-euEz9jeriuurnsZ

A fórmula de Bhaskara é um método resolutivo para equações do segundo grau utilizado para encontrar raízes a partir dos coeficientes da equação.
"""

#Baskara
def bsk():
  a =  float(input('Digite um número: '))
  b =  float(input('Digite um número: '))
  c =  float(input('Digite um número: '))
  delta = (b**2) - 4 * a * c
  x1 = (-(b) + (delta**0.5)) / 2 * a
  x2 = (-(b) - (delta**0.5)) / 2 * a
  print(f'O Delta é: {delta:.2f}')
  print(f'O x1 é: {x1:.2f}')
  print(f'O x2 é: {x2:.2f}')

#Velocidade média
def vlm():
  ds =  float(input('Digite o deslocamento (m): '))
  dt =  float(input('Digite o intervalo de tempo (s): '))
  vlm = ds / dt
  print(f'A velocidade média é: {vlm:.2f} m/s')

#Movimento retilíneo uniforme
def mru():
  so =  float(input('Digite a posição inicial (m): '))
  dv =  float(input('Digite a velocidade (m/s): '))
  dt =  float(input('Digite o intervalo de tempo (s): '))
  mru = so + (dv * dt)
  print(f'A posição final é: {mru:.2f} m')

#Movimento retilíneo uniformemente variado
def mruv():
  so =  float(input('Digite a posição inicial (m): '))
  dv =  float(input('Digite a velocidade inicial (m/s): '))
  da =  float(input('Digite a aceleração (m/s2): '))
  dt =  float(input('Digite o tempo (s): '))
  mruv = so + (dv * dt) + ((da * (dt**2))/2)
  print(f'A posição final é: {mruv:.2f} m')

#Quantidade de movimento
def qmo():
  dv =  float(input('Digite a velocidade (m/s): '))
  dm =  float(input('Digite a massa do objeto (g): '))
  dq =  ((dm / 1000) * dv)
  print(f'A quantidade de movimento do objeto é: {dq:.2f} kg.m/s')

#Fórmula da pressão hidrostática
#ds = 1g/cm3 = 1000kg/m3
def dph():
  ds =  float(input('Digite a densidade (kg/m³): '))
  da =  float(input('Digite a aceleração da gravidade (m/s²): '))
  dh =  float(input('Digite a altura (m): '))
  ph =  (ds*1000) * da * dh
  print(f'A quantidade de movimento do objeto é: {ph:.2f} N/m²')

dph()

