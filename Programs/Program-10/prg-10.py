import cv2
def crop(img_path, x, y, w, h):
  img = cv2.imread(img_path)
  cropped = img[y:y+h, x:x+w]
  cv2.imshow("Original Image",img)
  cv2.imshow("Cropped", cropped)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

crop("bmw.jpg", 20, 20, 150, 150)