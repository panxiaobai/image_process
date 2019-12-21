import cv2 as cv
import numpy as np

class region_div:
    def __init__(self,img):
        self.img=img
        self.res=np.zeros(img.shape)


    def region_div_group(self,range1,range2):
        if range1[1]-range1[0]==0 or range2[1]-range2[0]==0:
            return

        mean=self.img[range1[0]:range1[1],range2[0]:range2[1]].mean()
        var=self.img[range1[0]:range1[1],range2[0]:range2[1]].var()
        #print(self.img[range1[0]:range1[1],range2[0]:range2[1]])
        print(range1, range2,var)
        if var<10:
            self.res[range1[0]:range1[1],range2[0]:range2[1]]=255
        else:
            if range1[1]-range1[0]>=2 and range2[1]-range2[0]>=2:
                self.region_div_group([range1[0],(range1[0]+range1[1])//2],[range2[0],(range2[0]+range2[1])//2])
                self.region_div_group([ (range1[0] + range1[1]) // 2,range1[1]], [range2[0], (range2[0] + range2[1]) // 2])
                self.region_div_group( [range1[0], (range1[0] + range1[1]) // 2], [(range2[0] + range2[1]) // 2, range2[1]])
                self.region_div_group( [(range1[0] + range1[1]) // 2,range1[1]], [(range2[0] + range2[1]) // 2, range2[1]])


image = cv.imread('grow.png')
gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
print(gray.shape)
print(gray[0:1,5:11])
res=np.zeros(gray.shape)
rd=region_div(gray)
rd.region_div_group([0,gray.shape[0]],[0,gray.shape[1]])

res=rd.res
cv.namedWindow("gray")
cv.imshow("gray",gray)
cv.waitKey(0)

cv.namedWindow("res")
cv.imshow("res",res)
cv.waitKey(0)
