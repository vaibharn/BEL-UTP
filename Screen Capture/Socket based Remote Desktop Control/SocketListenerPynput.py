# -*- coding: utf-8 -*-

import numpy as np
import cv2
import time 
import pickle
import socket
import threading 
import logging 
import pynput 

logging.basicConfig(filename="ListenerLog.log",format='%(asctime)s %(message)s',filemode='w')
logger=logging.getLogger() 
logger.setLevel(logging.DEBUG)

ms = pynput.mouse.Controller()

def mouse_click(sock):
    logger.debug("mouse_click triggered")
    pos = ms.position
    raw_pos = pickle.dumps(pos)
    if len(raw_pos)==10:
        mc_trigger = b'ms_ck_10'
    elif len(raw_pos)==11:
        mc_trigger = b'ms_ck_11'
    else:
        mc_trigger = b'ms_ck_12'  
    sock.send(mc_trigger)
    sock.send(raw_pos)
    logger.debug("mouse_click ended")
    
def recvall(sock):
    raw_len=sock.recv(8)
    if not raw_len:
        return None
    logger.debug("recvd msg len")
    msg_len=pickle.loads(raw_len)
    data = b''
    while len(data) < msg_len:
        packet = sock.recv(msg_len-len(data))
        logger.debug("chunk")
        if not packet:
            return None
        data += packet
    logger.debug("recvall over")
    return data

def Main(): 
    s1=socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s2=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port1 = 12345
    port2 = 15432
    s1.connect(('127.0.0.1',port1))
    s2.bind(('',port2))
    print('socket binded to %s'%(port2)) 
    s2.listen()
    c, addr = s2.accept()
    mouse_listener = pynput.mouse.Listener(on_click=mouse_click(c))
    mouse_listener.start()
    logger.debug("started")
    while True:
        last_time=time.time()
        logger.debug("recvall started")
        raw_msg = recvall(s1)
        msg = pickle.loads(raw_msg)
        logger.debug("picke loaded")
        cv2.imshow('screen', np.array(msg))
        logger.debug("displayed img")
        try:
            print("fps: {}".format(1 / (time.time() - last_time)))
        except ZeroDivisionError:
            print("fps: -")
        mouse_listener.wait()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
    
    s1.close()
    pynput.mouse.Listener.stop()
if __name__=='__main__':
    Main()