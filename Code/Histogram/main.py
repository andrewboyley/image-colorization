from cv2 import cv2
from matplotlib import pyplot as plt
import numpy as np
import glob

image_dir = '/home/andrew/Pictures/Outputs/30_70'
files = [f for f in glob.glob(image_dir + "**/*.jpg")]

img = np.zeros((200, 200, 3))
for f in files:
    new_image = cv2.imread(f)
    new_image = cv2.resize(new_image, (200, 200), interpolation=cv2.INTER_AREA)

    img += new_image

img /= len(files)
img = np.floor(img).astype('int8')

b, g, r = cv2.split(img)

# alternative way to find histogram of an image 
plt.hist(b.ravel(), 50, [80, 130], color='blue')
plt.hist(g.ravel(), 50, [80, 130], color='green')
plt.hist(r.ravel(), 50, [80, 130], color='red')

# plt.imshow(img)
plt.ylim(0, 6000)
plt.show()
