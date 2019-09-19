# Importando o módulo matemático do python
import numpy as np
# Importando o opencv
import cv2
# Pegando a leitura da imagem
img = cv2.imread('cps.jpg')
# Transformando a imagem em cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Pegando o threshold da imagem
ret, thresh = cv2.threshold(gray, 127, 255, 0)
# Capturando os contornos da imagem
contours, hierarchy = cv2.findContours(
    thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# Mostrando quantos contornos tem a imagem
print(f"Número de contornos da imagem = {str(len(contours))} ")
# Desenhando na imagem os contornos
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
# Mostrando a imagem
cv2.imshow("imagem", img)
# Aperte 0 para fechar as janelas
cv2.waitKey(0)
cv2.destroyAllWindows()
