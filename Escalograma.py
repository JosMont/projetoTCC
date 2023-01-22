# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 09:08:11 2023

Gera um escalograma dos dados de vibração
"""
import pywt   # biblioteca do pywavelet 
import matplotlib.pyplot as plt  # módulo para criar os gráficos
import numpy as np   # módulo numpy
import pandas as pd   # módulo para lidar com data frames
import os     # módulo para trabalhar com diretórios

# 1 - Leitura dos dados
# Obter o diretório atual
cwd = os.getcwd()
print(cwd)

# Mudando para o diretorio dos dados em relação ao diretório atual.
os.chdir('../12k/B007')
cwd = os.getcwd()
print(cwd)

# nome dos arquivos csv que vamos carregar como data frame
nome = 'B007.csv'

# leitura do arquivo .csv com quatro colunas, sem header e espaço em branco como separador 
arquivo = pd.read_csv(nome, usecols=[0, 1, 2, 3], sep=' ', header=None) # lê o arquivo sem cabeçalho

print(arquivo.head(6))    # mostra as primeiras 6 linhas do data frame

# usando loc (pandas) para extrais uma amostra de 12.000 pontos 
# da coluna 0 do data frame.
dados_0 = arquivo.loc[0:(12000 - 1),0]

print(dados_0.head(10))   # mostra as primeiras 10 linhas da coluna de dados 0

# converte a serie de dados do pandas para um array do numpy
dados_0 = dados_0.to_numpy()

# Fazendo a transformada wavelet (CWT) e gerando o escalograma
#Toma 12000 amostras dos dados amostrados a 12 kHz
Fs = 12000.0
# Tamanho do sinal
N = len(dados_0)

#Parametros para CWT (continuous wavelet transform)
s = np.arange(2, 200)   #Escalas utilizadas (variando de 1 em 1)
wav = 'cmor5.0-1.0'  #Wavelet complexa de Morlet com B = 5.0 e C = 1.0

# Para evitar problemas de borda, vamos inserir amostras adicionais à série
# mais detelhes em: https://pywavelets.readthedocs.io/en/latest/ref/signal-extension-modes.html#ref-modes
amostras_pad = 600
serie_pad = pywt.pad(dados_0, amostras_pad, 'symmetric')

#Calcula a transformada wavelet contínua (CWT). 
# W são os coeficientes, o parametro _ seriam as freqs (frequencias)
C, _ = pywt.cwt(serie_pad, s, wav, method='fft') #C = coeficientes wavelet
W = np.abs(C)**2   # obtem o Escalograma

# Truanca W devido à operação de inserção de amostras (padding)
W = W[:, amostras_pad:-amostras_pad]

# Imprime a figura da série temporal e do escalograma
plt.figure(dpi=150, figsize=(18, 6))

# Série temporal
plt.subplot(121)
plt.plot(dados_0)
plt.xlabel('$f $ (amostra)')
plt.ylabel('$Amplitude$')
#plt.xlim([0, len(dados_0)])
plt.grid()

# Escalograma
plt.subplot(122)
plt.imshow(W, extent=[0, N, s[-1], s[0]], cmap='jet', aspect='auto')
plt.xlabel('Translação ($\\tau$)')
plt.ylabel('Escala ($s$)')
plt.ylim([s[-1], s[0]])
plt.xlim([0, len(dados_0)])
plt.colorbar()
plt.tight_layout()
plt.show()

# Salva o escalograma como uma imagem RGBA (198 X 12000 X 4)
# Essa imagem deve ser corrigida para RGB (224 X 224 X 3)
# Para isso vamos usar o script ResizeImage.py
plt.imsave('B007.png', W, format='png', cmap='jet')