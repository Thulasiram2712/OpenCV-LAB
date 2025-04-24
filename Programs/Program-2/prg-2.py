import cv2
from PIL import Image
img=cv2.imread('HP.jpg')
print("Image Height: ",img.shape[0])
print("Image Width: ",img.shape[1])
print("No. Of Channels: ",img.shape[2])
print("ImaSize (in Pixels): ",img.size)
print("Image Data Type: ",img.dtype)
img=Image.open('HP.jpg')
print("Image Format: ",img.format)