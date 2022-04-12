import cv2
import numpy as np

img = cv2.imread("gambar_tri.JPG")
img_1 = cv2.resize(img, (560, 340))
gray = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gambar Tri Original", img_1)
cv2.imshow("Gambar Tri GraScale", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()