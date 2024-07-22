import numpy as np
import matplotlib.pyplot as plt

from skimage import transform
from skimage.io import imread, imshow
import cv2

field_view = imread('images/1080_coop.png')
imshow(field_view) 
# plt.show()

# 1080_default
src = np.array([802, 163, # tl
                1126, 163, # tr
                653, 1040, # bl
                1271, 1040, # br
]).reshape((4, 2))

# Plot the points on the image with red color
plt.scatter(src[:, 0], src[:, 1], color='red', marker='o')

# 1080_default
dst = np.array([870, 150, # tl
                1030, 150, # tr
                870, 930, # bl
                1030, 930, # br
]).reshape((4, 2))

tform = transform.estimate_transform('projective', src, dst)

print(tform)
print(tform.inverse)

tf_img = transform.warp(field_view, tform.inverse) # in practice, use tform H matrix
fig, ax = plt.subplots()
# ax.scatter(dst[:, 0], dst[:, 1], color='red', marker='o')
ax.imshow(tf_img)
_ = ax.set_title('projective transformation')

plt.imshow(tf_img)
# # Plot the points on the image with red color
plt.scatter(dst[:, 0], dst[:, 1], color='red', marker='o')
plt.show()


