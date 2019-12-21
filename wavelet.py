import matplotlib.pyplot as plt  # plt 用于显示图片
import matplotlib.image as mpimg  # mpimg 用于读取图片
from PIL import Image
import numpy as np

img = Image.open('E:\\lena.jpg')


def wavelet_trans(grey_arr):
    l = np.zeros([grey_arr.shape[0], grey_arr.shape[1] // 2])

    for i in range(l.shape[0]):
        for j in range(l.shape[1]):
            l[i][j] = (grey_arr[i][2 * j] + grey_arr[i][2 * j + 1]) / 2


    h = np.zeros([grey_arr.shape[0], grey_arr.shape[1] // 2])
    for i in range(h.shape[0]):
        for j in range(h.shape[1]):
            h[i][j] = (grey_arr[i][2 * j] - grey_arr[i][2 * j + 1]) / 2


    ll = np.zeros([grey_arr.shape[0] // 2, grey_arr.shape[1] // 2])

    for i in range(ll.shape[0]):
        for j in range(ll.shape[1]):
            ll[i][j] = (l[2 * i][j] + l[2 * i + 1][j]) / 2


    lh = np.zeros([grey_arr.shape[0] // 2, grey_arr.shape[1] // 2])
    for i in range(lh.shape[0]):
        for j in range(lh.shape[1]):
            lh[i][j] = (l[2 * i][j] - l[2 * i + 1][j]) / 2


    hl = np.zeros([grey_arr.shape[0] // 2, grey_arr.shape[1] // 2])
    for i in range(hl.shape[0]):
        for j in range(hl.shape[1]):
            hl[i][j] = (h[2 * i][j] + h[2 * i + 1][j]) / 2


    hh = np.zeros([grey_arr.shape[0] // 2, grey_arr.shape[1] // 2])
    for i in range(hh.shape[0]):
        for j in range(hh.shape[1]):
            hh[i][j] = (h[2 * i][j] - h[2 * i + 1][j]) / 2


    return ll,lh,hl,hh

grey = img.convert('L')
# 此时 lena 就已经是一个 np.array 了，可以对它进行任意处理
grey_arr=np.array(grey)
trans_arr=grey_arr
for i in range(4):
    ll, lh, hl, hh=wavelet_trans(trans_arr)

    plt.figure('小波'+str(i+1)+'级变换')
    plt.subplot(2, 2, 1)
    plt.imshow(ll, cmap='Greys_r')
    plt.axis('off')  # 不显示坐标轴
    plt.subplot(2, 2, 2)
    plt.imshow(lh, cmap='Greys_r')
    plt.axis('off')  # 不显示坐标轴
    plt.subplot(2, 2, 3)
    plt.imshow(hl, cmap='Greys_r')
    plt.axis('off')  # 不显示坐标轴
    plt.subplot(2, 2, 4)
    plt.imshow(hh, cmap='Greys_r')
    plt.axis('off')  # 不显示坐标轴
    plt.show()
    trans_arr=ll


