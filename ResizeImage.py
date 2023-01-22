# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 13:42:17 2023

Muda as escalas de altura e comprimento e converte a imagem 
de RGBA (M X N X 4) para RGB (M X N X 3)

Informações obtidas nas seguintes páginas web:
https://cloudinary.com/guides/bulk-image-resize/python-image-resize-with-pillow-and-opencv
https://www.youtube.com/watch?v=4R7mA_AJxK8&list=LL&index=1&t=1265s
https://stackoverflow.com/questions/60757625/how-do-i-convert-an-rgba-image-to-rgb-and-feed-it-to-a-trained-cnn-in-keras
"""
import os     # módulo para trabalhar com diretórios
from PIL import Image
import matplotlib.pyplot as plt 

# Define o diretório onde se encontra a imagem original.
os.chdir('../12k/B007')
cwd = os.getcwd()
print(cwd)

# O formato da imagem original é RGBA (198 X 12000 X 4)
# Vamos converter para RGB e fazer um resize (224 X 224 X 3)
new_image = Image.open('B007.png').convert('RGB').resize((224, 224))

# Vamos salvar a imagem RGB no mesmo diretório da original
new_image.save('B007_new.png')

# Vamos carregar a iamgem RGB criada e verificar se o formato é (224 X 224 X 3)
new_image = plt.imread('B007_new.png')
plt.imshow(new_image)
plt.axis('off') # remove a numeração nos eixos da imagem
print(new_image.shape)   # fornece as dimensões da imagem: (224 X 224 X 3))
