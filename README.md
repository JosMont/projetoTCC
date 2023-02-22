# projetoTCC
Pasta para os arquivos de TCC de Data Science

As pastas B007, B014, B021, B028 contém arquivos com os dados para as esferas, com falhas de 0.07, 0.14, 0.21 e 0.28 polegadas

As pastas IR007, IR014, IR021, IR028 contém arquivos com os dados para o anel interno, com falhas de 0.07, 0.14, 0.21 e 0.28 polegadas

As pastas OR007, OR014, OR021 contém arquivos com os dados para o anel externo, com falhas de 0.07, 0.14 e 0.21 polegadas

A pasta normal contém arquivos com os dados para rolamentos sem defeito.

O diretório Data_frames contém o script CriaDataFrame.R que lê um conjunto de dados, cria um dataframe e salva um arquivo .csv.

Adicionados em 22/01/2023:

Scripts do Python:

SCRIPT Escalograma.py: lê um dos arquivos .csv gerado no RStudio, converte em um data frame usando a biblioteca Pandas. Um subconjunto de 12000 pontos é extraido de uma das colunas do data frame e uma transformada wavelet contínua é aplicada sobre esse subconjunto. O resultado é uma matriz W, que é plotada como um escalograma. O escalograma é salvo como uma imagem RGBA no formato (198 X 12000 X 4).

SCRIPT ResizeImage.py: Converte a imagem RGBA para RGB no formato (224 X 224 X 3).

SCRIPT EscalaParaFrequencia.py: script auxiliar para descobrir qual intervalo de frequências os valores de escala que estou usando cobrem.

Imagem_B014 - diretório com 76 imagens de Escalograma gerados a partir dos dados de elementos rolantes com falha de diâmetro 0,014 pol.
