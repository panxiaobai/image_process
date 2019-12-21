import cv2 as cv
import numpy as np

def thin(img):
    f=np.zeros([img.shape[0],img.shape[1]])
    m=np.zeros([img.shape[0],img.shape[1]])

    for i in range(1,img.shape[0]-1):
        for j in range(1,img.shape[1]-1):
            if img[i,j]==0:
                f[i][j]=min([f[i-1][j],f[i-1][j-1],f[i][j-1],f[i-1][j+1]])+1

    for i in range(img.shape[0]-2,0,-1):
        for j in range(img.shape[1]-2,0,-1):
            if img[i,j]==0:
                m[i][j]=min([m[i][j+1],m[i+1][j-1],m[i+1][j],m[i+1][j+1]])+1

    fm = np.zeros([img.shape[0], img.shape[1]])
    for i in range(0,fm.shape[0]):
        for j in range(0,fm.shape[1]):
            fm[i][j]=min(f[i][j],m[i][j])

    res=np.zeros([img.shape[0],img.shape[1]])

    for i in range(1,img.shape[0]-1):
        for j in range(1,img.shape[1]-1):
            if fm[i][j]>0 and fm[i][j]>=fm[i-1][j-1] and fm[i][j]>=fm[i-1][j] and fm[i][j]>=fm[i-1][j+1] and fm[i][j]>=fm[i][j-1] and fm[i][j]>=fm[i][j+1] and fm[i][j]>=fm[i+1][j-1] and fm[i][j]>=fm[i+1][j] and fm[i][j]>=fm[i+1][j+1]:
                res[i][j]=255

    return res


image = cv.imread('pikaqiu.png')
gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)

ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_TRIANGLE)


cv.namedWindow("Image")
cv.imshow("Image",image)
cv.waitKey(0)

cv.namedWindow("binary")
cv.imshow("binary",binary)
cv.waitKey(0)

res_img=thin(binary)

cv.namedWindow("res")
cv.imshow("res",res_img)
cv.waitKey(0)
