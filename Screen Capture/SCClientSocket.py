# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 10:39:09 2019

@author: Dell
"""
import socket 

from mss import mss
import numpy as np
import pickle
import struct 
    
s=socket.socket()
print('socket created')

port = 12345
bbox = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}

s.bind(('',port))

def send_msg(sock,msg):
    msg=struct.pack('>I',len(msg)) + msg
    sock.sendall(msg)

print('socket binded to %s'%(port))
s.listen(1)
print("Screen Capture started")
while(True):
    c, addr = s.accept()
    print('connected with ',addr)

    sct = mss()
    while True:
        sct_img = sct.grab(bbox)
        msg=pickle.dumps(sct_img)
        send_msg(c,msg)
c.close()
