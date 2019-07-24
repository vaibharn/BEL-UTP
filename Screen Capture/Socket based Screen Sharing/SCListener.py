# -*- coding: utf-8 -*-

import numpy as np
import cv2
import time 
import pickle
import socket
import threading 

def recvall(sock):
    raw_len=sock.recv(8)
    msg_len=pickle.loads(raw_len)
    data = b''
    while len(data) < msg_len:
        packet = sock.recv(msg_len-len(data))
        if not packet:
            return None
        data += packet
    return data

def Main(): 
    s=socket.socket()
    port = 12345
    s.connect(('192.168.122.1',port))

    while True:
        last_time=time.time()
        raw_msg = recvall(s)
        msg = pickle.loads(raw_msg)
        cv2.imshow('screen', np.array(msg))
        try:
            print("fps: {}".format(1 / (time.time() - last_time)))
        except ZeroDivisionError:
            print("fps: -")
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
    s.close()
    
if __name__=='__main__':
    Main()