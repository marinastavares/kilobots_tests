import cv2
import numpy as np
import cv2.aruco as aruco
import re
from testing_interface import x


# Fonte utilizada 
font = cv2.FONT_HERSHEY_SIMPLEX

# Tipo de dicionário utilizado no ArUco: Original
dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_ARUCO_ORIGINAL)

# Função para captar o video, para se utilizar a webcam, basta alterar para 0
cap = cv2.VideoCapture(x)

# Cria um dicionário, que liga keys - IDs - a um objeto
ListaKilobots = {}

try: 
    # checa se existe arquivo txt 
    fh = open('file.txt', 'w') 
except FileNotFoundError: 
    # caso não exista, cria
    fh= open("file.txt","w+")
    pass
    # limpa arquivo
    open('file.txt', 'w').close()

# While criado para percorrer cada frame do video
while True:
    
    # faz a leitura de cada frame do video
    ret, frame = cap.read()
    # Faz a conversão para o frame em escala cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Armazena em res os arucos detectados no frame, usando o dictionary
    res = aruco.detectMarkers(frame, dictionary) #res[0] refere-se aos corners e res[1] aos IDs

    # converte os valores de res em string, caso o valor for None, recebe 0
    Corners = str(0 if res[0] is None else res[0])
    # Armazena coordenadas, pega os valores de Corners e tira os \d que os separavam
    # Aqui os Corners estão posicionados em x e y do 1o canto do quadrado, 2o canto até o 4o canto, 
    # o 9 elemento será um retorno do tipo de instancia usada, no caso float
    Corners = [int(s) for s in re.findall(r'\d+', Corners)]
    
    # Na segunda posicao de res é armazenado o valor de ID do Aruco
    IDs = str(0 if res[1] is None else res[1])
    # Utiliza funcao para tirar separador \d
    IDs = [int(s) for s in re.findall(r'\d+', IDs)]


    # Cria uma instancia para checar se existem arucos, através do tamanho de red
    if len(res[0]) > 0:
        # Cara Aruco ocupa 9 posicoes em Corners, sendo assim o número de arucos sendo definidos
        # pela divisao do tamanho do array corners em 9
        i = int(len(Corners)/9)

        # Calculo do centro do Aruco
        for c in range(i):
            x1 = Corners[0+9*c] + Corners[2+9*c]
            x2 = Corners[4+9*c] + Corners[6+9*c]
            x = int(((x1 + x2)/4))

            y1 = Corners[1+9*c] + Corners[3+9*c]
            y2 = Corners[5+9*c] + Corners[7+9*c]
            y = int(((y1 + y2)/4))

            # Define que o key de ListaKilobots é de o ID do ArUco, e os valores junto a eles sao o x e y calculados
            ListaKilobots[IDs[c]] = (x,y)

            # Escreve as coordenadas em um arquivo txt
            # Escreve só os IDs diferentes de 0
            if (IDs[c] != 0): 
                fh.write(str(IDs[c]) + ' ' + 'Coor: ' + str(x) + ',' + str (y) + '\r')

            # Funcoes para escrever nos frames
            # Escreve título
            cv2.putText(frame,'Detection with ArUco Kilobots@UFSC',(50,50), font, 1,(0,0,0),1,cv2.LINE_AA)
            # Faz linha em volta dos kilobots
            cv2.circle(frame,(x, y), 30, (0,255,0), 1)
            # Escreve o ID
            cv2.putText(frame,str(IDs[c]),(x,y), font, 1,(255,255,255),2,cv2.LINE_AA)

            cv2.imshow('Aruco',frame)


    # funcao para sair do video
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()