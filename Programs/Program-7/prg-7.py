import cv2
def read_display_img(img_path):
    img=cv2.imread(img_path)
    if img is None:
        print("Error: Image not Found!")
        return
    cv2.imshow("Original Image",img)
    cv2.imwrite("Output_img.png",img)
    cv2.imwrite("Output_img.bmp", img)
    cv2.imwrite("Output_img.tiff", img)
    img_png=cv2.imread('Output_img.png')
    cv2.imshow("Image as PNG",img_png)
    img_bmp = cv2.imread('Output_img.bmp')
    cv2.imshow("Image as BMP", img_bmp)
    img_tiff = cv2.imread('Output_img.tiff')
    cv2.imshow("Image as TIFF", img_tiff)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
img_path='bmw.jpg'
read_display_img(img_path)