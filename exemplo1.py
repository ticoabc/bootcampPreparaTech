# -*- coding: utf-8 -*-
"""exemplo1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Wl-wL_vUtKHPHl_v-euEz9jeriuurnsZ

A fórmula de Bhaskara é um método resolutivo para equações do segundo grau utilizado para encontrar raízes a partir dos coeficientes da equação.
"""

def bsk():
  a =  int(input('Digite um número: '))
  b =  int(input('Digite um número: '))
  c =  int(input('Digite um número: '))
  delta = (b**2) - 4 * a * c
  print(delta)