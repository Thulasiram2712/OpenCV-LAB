import cv2
def edge_detection(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    cv2.imshow("Edges", cv2.Canny(img, 100, 200))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

edge_detection('bmw.jpg')