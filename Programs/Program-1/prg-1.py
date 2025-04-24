import cv2
def main():
    img=cv2.imread('HP.jpg')
    if img is None:
        print("Error: Could not read the Image")
        return
    res_img=cv2.resize(img,(250,250))
    cv2.imwrite("Resized_Image.jpg",res_img)
    print("Resized Image Saved")
    cv2.imshow("Original Image",img)
    cv2.imshow("Resized Image",res_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()