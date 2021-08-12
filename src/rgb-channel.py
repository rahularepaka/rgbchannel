from PIL import Image
import numpy as np
import cv2

im = np.array(Image.open('elon.jpg'))

im_R = im.copy()
im_R[:, :, (1, 2)] = 0
im_G = im.copy()
im_G[:, :, (0, 2)] = 0
im_B = im.copy()
im_B[:, :, (0, 1)] = 0

im_RGB = np.concatenate((im_R, im_G, im_B), axis=1)
# im_RGB = np.hstack((im_R, im_G, im_B))
# im_RGB = np.c_['1', im_R, im_G, im_B]

cv2.imshow("R", im_R)
cv2.imshow("G", im_G)
cv2.imshow("B", im_B)


cv2.waitKey(0)
cv2.destroyAllWindows()
