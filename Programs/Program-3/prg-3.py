import cv2
def main():
    img=cv2.imread('HP.jpg')
    if img is None:
        print("Error: Could not read the Image")
        return
    gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Original Image",img)
    cv2.imshow("Grayscale Image",gray_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()