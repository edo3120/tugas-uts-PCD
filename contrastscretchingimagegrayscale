import cv2
image = cv2.imread("butterfly_flower_gray.jpg")
cv2.normalize(image, image, alpha=20, beta=200, norm_type=cv2.NORM_MINMAX)
cv2.namedWindow("TestWindow", cv2.WINDOW_AUTOSIZE)
cv2.imshow("Test", image)
cv2.waitKey(0)
