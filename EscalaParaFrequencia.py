# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 10:39:03 2023

Estudo da relação entre escalas e frequências nos sinais da CWRU
"""
import pywt
import numpy as np   # módulo numpy

#Frequência de amostragem
Fs = 12000

#Parametros para CWT
s = np.arange(2, 200)   #Escolhe o intervalo das escalas s
wav = 'cmor5.0-1.0'  #Wavelet complexa de Morlet com B = 5.0 e C = 1.0

#Mostra as frequências cobertas para a wavelet e escalas selecionadas
fre = pywt.scale2frequency(wav, s) * Fs  # Converte escalas para frequências
print('Escala - Frequência')
for i, item in enumerate(s):
    print('[%.2f, %.2f]' %(item, fre[i]))