import cv2 as cv

trained_face_data = cv.CascadeClassifier('frontalface.xml')


face = cv.imread('my_face.jpeg')
cv.imshow('My face', face)
# cv.waitKey()
