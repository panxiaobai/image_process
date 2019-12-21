import cv2 as cv
import numpy as np

def region_seed_grow(img,seed,low_bound,high_bound):
    stack=[seed]

    res=np.zeros(img.shape)

    while stack:
        s=stack.pop()
        i=s[0]
        j=s[1]
        res[i][j]=255
        #print(i,j)
        if i!=0 and j!=0 and res[i-1][j-1]==0 and abs(int(img[i][j])-int(img[i-1][j-1]))>=low_bound and abs(int(img[i][j])-int(img[i-1][j-1]))<=high_bound:
            stack.append([i-1,j-1])
        if i!=0 and res[i-1][j]==0 and abs(int(img[i][j])-int(img[i-1][j]))>=low_bound and abs(int(img[i][j])-int(img[i-1][j]))<=high_bound:
            stack.append([i-1,j])
        if i!=0 and j!=img.shape[1]-1 and res[i-1][j+1]==0 and abs(int(img[i][j])-int(img[i-1][j+1]))>=low_bound and abs(int(img[i][j])-int(img[i-1][j+1]))<=high_bound:
            stack.append([i-1,j+1])
        if j!=0 and res[i][j-1]==0 and abs(int(img[i][j])-int(img[i][j-1]))>=low_bound and abs(int(img[i][j])-int(img[i][j-1]))<=high_bound:
            stack.append([i,j-1])
        if j!=img.shape[1]-1 and res[i][j+1]==0 and abs(int(img[i][j])-int(img[i][j+1]))>=low_bound and abs(int(img[i][j])-int(img[i][j+1]))<=high_bound:
            stack.append([i,j+1])
        if i!=img.shape[0]-1 and j!=0 and res[i+1][j-1]==0 and abs(int(img[i][j])-int(img[i+1][j-1]))>=low_bound and abs(int(img[i][j])-int(img[i+1][j-1]))<=high_bound:
            stack.append([i+1,j-1])
        if i!=img.shape[0]-1 and res[i+1][j]==0 and abs(int(img[i][j])-int(img[i+1][j]))>=low_bound and abs(int(img[i][j])-int(img[i+1][j]))<=high_bound:
            stack.append([i+1,j])
        if i!=img.shape[0]-1 and j!=img.shape[1]-1 and res[i+1][j+1]==0 and abs(int(img[i][j])-int(img[i+1][j+1]))>=low_bound and abs(int(img[i][j])-int(img[i+1][j+1]))<=high_bound:
            stack.append([i+1,j+1])

    return res


image = cv.imread('grow.png')
gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)

res=region_seed_grow(gray,[60,580],0,10)

cv.namedWindow("gray")
cv.imshow("gray",gray)
cv.waitKey(0)

cv.namedWindow("res")
cv.imshow("res",res)
cv.waitKey(0)



