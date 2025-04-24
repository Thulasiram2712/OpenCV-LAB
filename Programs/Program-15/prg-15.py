import easyocr
import cv2
import matplotlib.pyplot as plt

# Initialize EasyOCR reader and load image
reader = easyocr.Reader(['en'])
image = cv2.imread('sample.tiff')

# Detect text and draw bounding boxes
for bbox, text, _ in reader.readtext(image):
    cv2.rectangle(image, tuple(map(int, bbox[0])), tuple(map(int, bbox[2])), (0, 255, 0), 2)
    cv2.putText(image, text, (int(bbox[0][0]), int(bbox[0][1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Display the result
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()