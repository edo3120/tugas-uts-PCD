import cv2
image = cv2.imread('butterfly_flower.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('butterfly_flower_gray.jpg',gray_image)
cv2.imshow('color_image',image)
cv2.imshow('gray_image',gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
