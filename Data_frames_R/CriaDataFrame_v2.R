# Instalação e carregamento dos pacotes utilizados

pacotes <- c("tidyverse", #carregar outros pacotes do R
             "R.matlab") #abrir arquivos matlab
             
if(sum(as.numeric(!pacotes %in% installed.packages())) != 0){
  instalador <- pacotes[!pacotes %in% installed.packages()]
  for(i in 1:length(instalador)) {
    install.packages(instalador, dependencies = T)
    break()}
  sapply(pacotes, require, character = T) 
} else {
  sapply(pacotes, require, character = T) 
}

# OBSERVAÇÃO:
# Os arquivos Normal foram extraidos separadamente por não haver
# uma regularidade entre eles e os arquivos extraidos com este script.

# Passando os diretoórios onde se encontram os arquivos de dados
setwd("D:/RollingBearingDatasets/CWRU/12k/B007")
# setwd("D:/RollingBearingDatasets/CWRU/12k/B014")  
# setwd("D:/RollingBearingDatasets/CWRU/12k/B021")
# setwd("D:/RollingBearingDatasets/CWRU/12k/IR007")
# setwd("D:/RollingBearingDatasets/CWRU/12k/IR014")  
# setwd("D:/RollingBearingDatasets/CWRU/12k/IR021")
# setwd("D:/RollingBearingDatasets/CWRU/12k/OR007@6")
# setwd("D:/RollingBearingDatasets/CWRU/12k/OR014@6")  
# setwd("D:/RollingBearingDatasets/CWRU/12k/OR021@6")

wd = getwd()
print(wd)    # examina se o diretório atual está correto

# Nome para o arquivo de saída. A extensão será atribuida mais adiante
file_name = "B007"
# file_name = "B014"
# file_name = "B021"
# file_name = "IR007"
# file_name = "IR014"
# file_name = "IR021"
# file_name = "OR007@6"
# file_name = "OR014@6"
# file_name = "OR021@6"

# Lê os arquivos .mat do diretório atual. 
# Os nomes dos arquivos devem ser alterados manualmente para cada conjunto de dados
# Sempre nomear em ordem crescente
Dados1 <- readMat("118.mat")
Dados2 <- readMat("119.mat")
Dados3 <- readMat("120.mat")
Dados4 <- readMat("121.mat")

# Examinando os arquivos - Listas com 4 objetos
View(Dados1)
View(Dados2)
View(Dados3)
View(Dados4)

# Extraindo as velocidades de rotação de cada conjunto de dados como character
rpm_1 <- Dados1[[4]]
rpm_2 <- Dados2[[4]]
rpm_3 <- Dados3[[4]]
rpm_4 <- Dados4[[4]]

# Criando dataframes com 4 variáveis (drive-end (DE), fan-end (FE), base(BA) e rpm)
df_1 <- data.frame(Dados1)
df_2 <- data.frame(Dados2)
df_3 <- data.frame(Dados3)
df_4 <- data.frame(Dados4)

# Determinando o número de linhas de cada dataframe
# Observe que o número de linhas não é o mesmo em todos os datasets
n1 <- nrow(df_1)
n2 <- nrow(df_2)
n3 <- nrow(df_3)
n4 <- nrow(df_4)

# Removendo linhas acima de 120000 para uniformizar os dataframes
df_1 <- df_1 %>% filter(!row_number() %in% c(120001:n1))

# Removendo as colunas 2 (FE), 3 (BA) e 4 (RPM)
df_1 <- df_1[, -c(2:4)]

# Repetindo o procedimento para os três conjuntos de dados restantes
df_2 <- df_2 %>%  filter(!row_number() %in% c(120001:n2))
df_2 <- df_2[, -c(2:4)]

df_3 <- df_3 %>%  filter(!row_number() %in% c(120001:n3))
df_3 <- df_3[, -c(2:4)]

df_4 <- df_4 %>%  filter(!row_number() %in% c(120001:n4))
df_4 <- df_4[, -c(2:4)]

df_final <- data.frame(df_1, df_2, df_3, df_4)

# Mudando os nomes das colunas, para indicar as velocidades de rotação usadas
# As velocidades são sempre as mesmas em todos os conjuntos de dados
colnames(df_final) <- c(rpm_1, rpm_2, rpm_3, rpm_4)
view(df_final)

# Procurando missing values (NA)
sum(is.na(df_final))

# Examinando os tipos de dados nas colunas
typeof(df_final[1:120000, 1])
typeof(df_final[1:120000, 2])
typeof(df_final[1:120000, 3])
typeof(df_final[1:120000, 4])

# Inserindo a extensão .csv no nome do arquivo que será salvo no diretório
file_name_csv = paste(file_name, "csv", sep=".")

# Salvando o arquivo como csv no mesmo diretório onde estão os dados
write.table(df_final,file_name_csv,row.names=F, col.names=F)



