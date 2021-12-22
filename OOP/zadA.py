from PIL import Image, ImageFilter
import numpy as np

image = Image.open('../corsa.jpg')  # wczytanie obrazka (format obojętny)
# image.show()  # wyświetlenie obrazka
data = np.asarray(image)  # zamiana obrazka na tablicę numpy
print(data.shape)  # np. (128, 128, 3), lub (128, 128, 4) jeśli jest alpha

img1 = Image.fromarray(data, 'RGB')  # lub 'RGBA' jeśli jest alpha, lub pominąć jeśli jest czarno-biały
img1.show()