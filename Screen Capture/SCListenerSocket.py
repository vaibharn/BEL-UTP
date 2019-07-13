# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 10:39:54 2019

@author: Dell
"""

import numpy as np
import cv2
import time 
import pickle
import socket 
import struct 

def recv_msg(sock):
    raw_msglen = recvall(sock, 4)
    if not raw_msglen:
        return None
    msglen = struct.unpack('>I', raw_msglen)[0]
    return recvall(sock, msglen)

def recvall(sock, n):
    data = b''
    while len(data) < n:
        packet = sock.recv(n-len(data))
        if not packet:
            return None
        data += packet
    return data
    
s=socket.socket()

port = 12345

s.connect(('127.0.0.1',port))

while True:
    last_time=time.time()
    msg = recv_msg(s)
    msg2=pickle.loads(msg)
    cv2.imshow('screen', np.array(msg2))
    
    try:
        print("fps: {}".format(1 / (time.time() - last_time)))
    except ZeroDivisionError:
        print("fps: -")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
    
s.close()