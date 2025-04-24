import cv2 as cv
import matplotlib.pyplot as pl
def show_hist(p):
  i = cv.imread(p)
  if i is None: return print(f'Err: {p}')
  for c, l in enumerate('bgr'):
    pl.plot(cv.calcHist([i], [c], None, [256], [0, 256]), color=l, label=l)
  pl.title('Histogram')
  pl.xlabel('Value')
  pl.ylabel('Freq')
  pl.legend()
  pl.grid()
  pl.show()
show_hist('bmw.jpg')