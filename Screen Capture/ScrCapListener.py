from multiprocessing.connection import Listener
import numpy as np
import cv2

address = ('localhost', 6000)
listener = Listener(address, authkey=b'secret password')
conn = listener.accept()
print("connection accepted from", listener.last_accepted)
while True:
    msg = conn.recv()
    print(msg)
    cv2.imshow('screen', np.array(msg))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
conn.close()   
listener.close()