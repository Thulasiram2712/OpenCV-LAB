import cv2
def flip_img(path):
    orig = cv2.imread(path)
    flip_codes = [1, 0, -1]
    flip_titles = ["Flip-Horiz", "Flip-Vert", "Flip-Both"]
    cv2.imshow("Original", orig)
    for code, title in zip(flip_codes, flip_titles):
        cv2.imshow(title, cv2.flip(orig, code))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
flip_img("lion.png")