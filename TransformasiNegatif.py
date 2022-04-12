import cv2

img = cv2.imread("gambar_tri2.JPG")
img_1 = cv2.resize(img, (560, 340))
img_2 = 255 - img_1

cv2.imshow("Gambar Tri Original", img_1)
cv2.imshow("Gambar Negatif", img_2)

cv2.waitKey()
cv2.destroyAllWindows()