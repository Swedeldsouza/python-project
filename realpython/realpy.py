import cv2
import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import colors
nemo = cv2.imread('nemo.jpg')  #default reads images in BGR format.
plt.imshow(nemo)
plt.show()

#use the cvtColor(image, flag) and the flag we looked at above to fix this:

nemo = cv2.cvtColor(nemo, cv2.COLOR_BGR2RGB)
plt.imshow(nemo)
plt.show()




'''+
Visualizing Nemo in RGB Color Space

HSV is a good choice of color space for segmenting by color
compare the image in both RGB and HSV color spaces by visualizing 
the color distribution of its pixels. A 3D plot shows this quite nicely
, with each axis representing one of the channels in the color space.
 If you want to know how to make a 3D plot, view the collapsed section
 
 
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import colors




OpenCV split() is very handy here; 
it splits an image into its component channels.
 These few lines of code split the image and set up the 3D plot:
     
     
'''
r, g, b = cv2.split(nemo)
fig = plt.figure()
axis = fig.add_subplot(1, 1, 1, projection="3d")



pixel_colors = nemo.reshape((np.shape(nemo)[0]*np.shape(nemo)[1], 3))
norm = colors.Normalize(vmin=-1.,vmax=1.)
norm.autoscale(pixel_colors)
pixel_colors = norm(pixel_colors).tolist()



axis.scatter(r.flatten(), g.flatten(), b.flatten(), facecolors=pixel_colors, marker=".")
axis.set_xlabel("Red")
axis.set_ylabel("Green")
axis.set_zlabel("Blue")
plt.show()





#To convert an image from RGB to HSV, you can use cvtColor():

hsv_nemo = cv2.cvtColor(nemo, cv2.COLOR_RGB2HSV)


h, s, v = cv2.split(hsv_nemo)
fig = plt.figure()
axis = fig.add_subplot(1, 1, 1, projection="3d")

axis.scatter(h.flatten(), s.flatten(), v.flatten(), facecolors=pixel_colors, marker=".")
axis.set_xlabel("Hue")
axis.set_ylabel("Saturation")
axis.set_zlabel("Value")
plt.show()



#Picking  out a range
light_orange = (1, 190, 200)
dark_orange = (18, 255, 255)

from matplotlib.colors import hsv_to_rgb

lo_square = np.full((10, 10, 3), light_orange, dtype=np.uint8) / 255.0
do_square = np.full((10, 10, 3), dark_orange, dtype=np.uint8) / 255.0



plt.subplot(1, 2, 1)
plt.imshow(hsv_to_rgb(do_square))
plt.subplot(1, 2, 2)
plt.imshow(hsv_to_rgb(lo_square))
plt.show()



mask = cv2.inRange(hsv_nemo, light_orange, dark_orange)
result = cv2.bitwise_and(nemo, nemo, mask=mask)

plt.subplot(1, 2, 1)
plt.imshow(mask, cmap="gray")
plt.subplot(1, 2, 2)
plt.imshow(result)
plt.show()




















































