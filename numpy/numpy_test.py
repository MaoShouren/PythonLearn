import numpy as np
import cv2

img = cv2.imread("000000.png")

print("img.shape", img.shape) # (375, 1242, 3)
# img_splice = img[:, :, ::-1] # 在最后一个维度上逆序，从 RGB -> BGR
# img_splice = img[::-1, ::-1, :] # 可以颠倒图像
# img_splice = img[0:200, 0:600, :] # 可以裁减图片
# img_splice = img[:, :, 2] # 取出特定的通道
img_splice = img[::2, ::2, :] # 行列各少一半
new_img = np.ascontiguousarray(img_splice)
img_new = img.transpose(2,0,1) # (375, 1242, 3)

cv2.imshow("img", img) #
cv2.imshow("new_img", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()



