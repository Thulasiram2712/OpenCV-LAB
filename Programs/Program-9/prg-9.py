import cv2
def show_rotated_right(img_path, angle):
  img = cv2.imread(img_path)
  h, w = img.shape[:2]
  M = cv2.getRotationMatrix2D((w/2, h/2), -angle, 1)
  rotated = cv2.warpAffine(img, M, (w, h))
  cv2.imshow("Rotated Right", rotated)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
show_rotated_right("HP.jpg", 45)