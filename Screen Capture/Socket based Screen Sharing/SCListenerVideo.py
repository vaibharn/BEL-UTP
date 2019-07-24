# -*- coding: utf-8 -*-

import numpy as np
import cv2
import time 
import pickle
import socket


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
    height = 768
    width = 1366
    s.connect(('127.0.0.1',port))
    vidname =str(time.time()) + ".avi"
    output = vidname
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output, fourcc, 5, (width, height))
    while True:
        last_time=time.time()
        raw_msg = recvall(s)
        msg = pickle.loads(raw_msg)
        img = np.array(msg)
        image = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        image2 = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        out.write(image2)
        cv2.imshow('screen', img)
        try:
            print("fps: {}".format(1 / (time.time() - last_time)))
        except ZeroDivisionError:
            print("fps: -")
        if cv2.waitKey(1) & 0xFF == ord('q'):
            out.release()
            cv2.destroyAllWindows()
            break
    s.close()
    
if __name__=='__main__':
    Main()