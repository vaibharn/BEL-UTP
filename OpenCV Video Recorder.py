import cv2
import numpy as np
import time
from mss import mss

bbox = {'top': 0, 'left': 0, 'width': 1366, 'height': 768}
vidname =str(time.time()) + ".avi"
output = vidname
sct = mss()
img = sct.grab(bbox)
img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
#get info from img
height, width, channels = img.shape
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output, fourcc,5, (width, height))

while(True):
 try:
  img = sct.grab(bbox)
  image = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
  image2 = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
  out.write(image2)
  StopIteration(0.5)
 except KeyboardInterrupt:
  break

out.release()
cv2.destroyAllWindows()