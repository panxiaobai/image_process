import cv2 as cv
import numpy as np

import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(1000000)

class Watershed:

    def __init__(self,img):
        self.img=img
        self.res=np.zeros(img.shape)



    def travel_point(self,i,j,lead_id,threshold,from_local):
        if i>=0 and i<self.img.shape[0] and j>=0 and j<self.img.shape[1]:
            if self.img[i][j]<=threshold:
                if self.res[i][j]==255 or self.leak_map[i][j]==lead_id+1:
                    return
                #print(i,j)
                if self.leak_map[i][j]==0:
                    self.leak_map[i][j]=lead_id+1
                    self.travel_leak(lead_id, [i, j], threshold,from_local)
                elif self.leak_map[i][j]!=lead_id+1:
                    self.res[i][j]=255


    def travel_leak(self,lead_id,s_point,threshold,from_local):
        #print(level)
        i=s_point[0]
        j=s_point[1]
        if from_local==0:
            self.travel_point(i-1,j-1,lead_id,threshold,1)
            self.travel_point(i - 1, j , lead_id, threshold,2)
            self.travel_point(i - 1, j + 1, lead_id, threshold,3)
            self.travel_point(i , j - 1, lead_id, threshold,8)
            self.travel_point(i , j + 1, lead_id, threshold,4)
            self.travel_point(i + 1, j - 1, lead_id, threshold,7)
            self.travel_point(i + 1, j , lead_id, threshold,6)
            self.travel_point(i + 1, j + 1, lead_id, threshold,5)
        elif from_local==1:
            self.travel_point(i - 1, j - 1, lead_id, threshold, 1)
            self.travel_point(i - 1, j, lead_id, threshold, 2)
            self.travel_point(i, j - 1, lead_id, threshold, 8)
        elif from_local==2:
            self.travel_point(i - 1, j, lead_id, threshold, 2)
        elif from_local==3:
            self.travel_point(i - 1, j, lead_id, threshold, 2)
            self.travel_point(i - 1, j + 1, lead_id, threshold, 3)
            self.travel_point(i, j + 1, lead_id, threshold, 4)
        elif from_local==4:
            self.travel_point(i, j + 1, lead_id, threshold, 4)
        elif from_local==5:
            self.travel_point(i + 1, j, lead_id, threshold, 6)
            self.travel_point(i + 1, j + 1, lead_id, threshold, 5)
            self.travel_point(i, j + 1, lead_id, threshold, 4)
        elif from_local==6:
            self.travel_point(i + 1, j, lead_id, threshold, 6)
        elif from_local==7:
            self.travel_point(i + 1, j - 1, lead_id, threshold, 7)
            self.travel_point(i + 1, j, lead_id, threshold, 6)
            self.travel_point(i, j - 1, lead_id, threshold, 8)
        elif from_local==8:
            self.travel_point(i, j - 1, lead_id, threshold, 8)

    def watershed(self):
        self.leak_map=np.zeros(self.img.shape)
        self.leak_point_list=[]
        threshold=255
        for i in range(1,self.img.shape[0]-1):
            for j in range(1,self.img.shape[1]-1):
                if self.img[i][j]<self.img[i][j+1] and self.img[i][j]<self.img[i][j-1] and self.img[i][j]<self.img[i-1][j-1] and self.img[i][j]<self.img[i-1][j] and self.img[i][j]<self.img[i-1][j+1] and self.img[i][j]<self.img[i+1][j-1] and self.img[i][j]<self.img[i+1][j] and self.img[i][j]<self.img[i+1][j+1]:
                    self.leak_map[i][j]=len(self.leak_point_list)+1
                    self.leak_point_list.append([i,j])
                    threshold=min(threshold,self.img[i][j])
        #print(len(self.leak_point_list))
        while threshold!=100:
            for i in range(len(self.leak_point_list)):
                #print(i)
                self.travel_leak(i,self.leak_point_list[i],threshold,0)
            print(threshold)
            threshold+=1

        return self.res


image = cv.imread('grow.png')
gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)

ws=Watershed(gray)
res=ws.watershed()

cv.namedWindow("gray")
cv.imshow("gray",gray)

cv.namedWindow("res")
cv.imshow("res",res)



ws.leak_map=(ws.leak_map-ws.leak_map.min())/(ws.leak_map.max()-ws.leak_map.min())*255
print(ws.leak_map.max())
print(ws.leak_map.min())

cv.namedWindow("leak")
cv.imshow("leak",ws.leak_map)



plt.imshow(ws.leak_map)
plt.show()
cv.waitKey(0)






