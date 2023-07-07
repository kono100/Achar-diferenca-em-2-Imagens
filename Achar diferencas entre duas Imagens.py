import cv2
import numpy as np

# Carregar as duas imagens
image1 = cv2.imread('C:/Users/User/Downloads/Img2.jpg')
image2 = cv2.imread('C:/Users/User/Downloads/Img1.jpg')

# Verificar se as imagens têm o mesmo tamanho
if image1 is not None and image2 is not None and image1.shape == image2.shape:
    # Calcular a diferença absoluta entre as duas imagens
    diff = cv2.absdiff(image1, image2)

    # Converter a imagem de diferença para escala de cinza
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    # Aplicar uma limiarização para destacar as diferenças
    _, thresh = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)

    # Encontrar contornos das diferenças
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Desenhar contornos na imagem original
    cv2.drawContours(image1, contours, -1, (0, 0, 255), 2)

    # Redimensionar a imagem para um tamanho adequado
    scale_percent = 50  # Por exemplo, redimensionar para 50% do tamanho original
    width = int(image1.shape[1] * scale_percent / 100)
    height = int(image1.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized_image = cv2.resize(image1, dim, interpolation=cv2.INTER_AREA)

    # Mostrar a imagem redimensionada com as diferenças destacadas
    cv2.imshow('Diferenças', resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Salvar a nova imagem redimensionada com as diferenças destacadas
    cv2.imwrite('C:/Users/User/Downloads/Imagem_diferencas.jpg', resized_image)
else:
    print("Erro ao carregar as imagens ou as imagens têm tamanhos diferentes.")
