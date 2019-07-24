from multiprocessing.connection import Listener
import numpy as np
import cv2
import time 

address = ('localhost', 6000)
listener = Listener(address, authkey=b'password')
conn = listener.accept()
print("connection accepted from", listener.last_accepted)
while True:
    last_time=time.time()
    msg = conn.recv()
    cv2.imshow('screen', np.array(msg))
    
    try:
        print("fps: {}".format(1 / (time.time() - last_time)))
    except ZeroDivisionError:
        print("fps: -")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
conn.close()   
listener.close()