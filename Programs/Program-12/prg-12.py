import cv2
image = cv2.imread('lion.png')
cv2.imshow('Original Image', image)
gaussian_blur = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow('Gaussian Blur', gaussian_blur)
median_blur = cv2.medianBlur(image, 5)  # 5x5 kernel
cv2.imshow('Median Blur', median_blur)
bilateral_blur = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imshow('Bilateral Filter', bilateral_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()