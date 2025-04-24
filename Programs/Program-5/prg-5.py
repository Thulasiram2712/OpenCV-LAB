import cv2
import numpy as np
img=np.ones((500,500,3),dtype="uint8")*255
cv2.line(img,(50,50),(450,450),(0,0,255),5)
cv2.circle(img,(250,250),100,(0,255,0),3)
cv2.rectangle(img,(50,400),(450,450),(255,0,0),-1)
cv2.rectangle(img,(100,100),(400,400),(0,255,255),5)
cv2.imshow("Image With Shapes",img)
cv2.waitKey(0)
cv2.destroyAllWindows()