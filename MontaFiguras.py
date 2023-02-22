# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 13:20:52 2023

Programa para gerar as imagens RGB dos Escalograms das séries temporais
"""
import time    # módulo para cronometrar o tempo de execução
import pywt    # biblioteca pywavelet
from PIL import Image   # módulo para convertes as imagens para imagens RGB
import matplotlib.pyplot as plt  # módulo para criar os gráficos
import numpy as np   # módulo numpy
import pandas as pd   # módulo para lidar com data frames
import os     # módulo para trabalhar com diretórios

# Função para calcular a transformada Wavelet contínua:
def ContWavelTranf(dados, s, wav, Ts):
    # Para evitar problemas de borda, vamos inserir amostras adicionais à série
    # mais detelhes em: https://pywavelets.readthedocs.io/en/latest/ref/signal-extension-modes.html#ref-modes
    amostras_pad = 1200
    serie_pad = pywt.pad(dados, amostras_pad, 'symmetric')

    #Computa a transformada Wavelet contínua (CWT). 
    # W são os coeficientes, o parametro _ seriam as freqs (frequencias)
    C, _ = pywt.cwt(serie_pad, s, wav, sampling_period = Ts, method='fft') #coeficientes wavelet
    W = np.abs(C)**2   # obtem o Escalograma

    # Truanca W devido à operação de inserção de amostras (padding)
    W = W[:, amostras_pad:-amostras_pad]
    return W

# função que cria o escalograma e o converte em imagem RGB 224 X 224
def GeraImagemRGB(W, nome_imagem, nome_RGB):
    # Criando o escalograma a partir de W
    plt.imsave(nome_imagem, W, format='png', cmap='jet')

    # O formato da imagem criada é RGBA (198 X 12000 X 4)
    # Vamos converter para RGB e fazer um resize (224 X 224 X 3)
    new_image = Image.open(nome_imagem).convert('RGB').resize((224, 224))

    # Vamos salvar a imagem RGB no mesmo diretório da original
    new_image.save(f'{nome_RGB}.png')

# Cronometrar quanto tempo o programa leva para executar.
instante_inicial = time.time()

# dir1 = '../12k/IR'
# dir1 = '../12k/OR'
dir1 = '../12k/B'
# dir1 = '../12k/Normal'

# Diretorio dos dados em relação ao diretório atual.
os.chdir(dir1)

# nome dos arquivos csv que serão lidos
# nome = 'Normal'
# nome = 'B007'
nome = 'B014'
# nome = 'B021'
# nome = 'OR007'
# nome = 'OR014'
# nome = 'OR021'
# nome = 'IR007'
# nome = 'IR014'
# nome = 'IR021'

# combinando o nome dos arquivos com sua extensão
nome_arquivo = '{}.csv'.format(nome) # arquivo .csv da base de dados
nome_imagem = '{}.png'.format(nome)  # arquivo .png da imagem gerada (escalograma)

# Lendo banco de dados .csv com quatro colunas, 
# sem header (header=None) e espaço em branco como separador
arquivo = pd.read_csv(nome_arquivo, usecols=[0, 1, 2, 3], sep=' ', header = None)

# Parâmetros para a transformada wavelet contínua:
# Taxa de amostragem de 12 kHz:
Fs = 12000.0
# Período de amostragem:
Ts = 1.0/Fs
# Intervalo de escalas s para a CWT
s = np.arange(64, 512, 1)   #Escalas s utilizadas
# Tipo de Wavelet usada:
wav = 'cmor5.0-1.0'  #Wavelet complexa de Morlet com B = 5.0 e C = 1.0

# usando loc (pandas) para extrais uma amostra de 12.000 pontos 
# da coluna n do data frame. Os 6.000 pontos finais serão incluidos
# novamente na próxima amostra.

nome_RGB = 0
for n in np.arange(0, 4):   # em range o valor final (4) não é incluído
    for inicio in np.arange(0, 120000 - 6000, 6000):
        final = inicio + 12000
        dados = arquivo.loc[inicio:(final - 1), n]  # Lendo 12 mil linhas de dados
        # convertendo as series de dados do pandas para um array do numpy
        dados = dados.to_numpy()
        
        # Obtendo a matriz W da CWT
        W = ContWavelTranf(dados, s, wav, Ts)
        
        # Gerando os escalogramas como igagens RGB 
        # Mudando o diretório para o de imagens
        dir2 = (f'../../Figuras/{nome}')
        # Diretorio dos dados em relação ao diretório atual.
        os.chdir(dir2)
        nome_RGB = nome_RGB + 1  # nomeia as imagens numericamente (1.png, 2.png, ...)
        GeraImagemRGB(W, nome_imagem, nome_RGB)  # Cria a imagem no diretório definido
        
print("--- %s segundos ---" % (time.time() - instante_inicial))

        
        
        
    
    
    
    
    
    
    
    
    
    
    
    