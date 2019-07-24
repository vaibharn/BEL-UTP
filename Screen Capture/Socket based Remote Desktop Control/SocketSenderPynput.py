# -*- coding: utf-8 -*-

import socket 
from mss import mss
import pickle
import logging 
import pynput

logging.basicConfig(filename="ClientLog.log",format='%(asctime)s %(message)s',filemode='w')
logger=logging.getLogger() 
logger.setLevel(logging.DEBUG) 

ms = pynput.mouse.Controller()
def recms(sock):
    logger.debug('recms called')
    mc_trigger = sock.recv(8)
    if not mc_trigger:
        return None
    logger.debug("mc_trigger recvd")
    if mc_trigger==b'ms_ck_10':
        logger.debug('recms 1')
        raw_pos = sock.recv(10)
        if not raw_pos:
            return None
        pos = pickle.loads(raw_pos)
        ms.position = pos
        ms.click(pynput.mouse.Button.left,1)
        print(ms.position)
    elif mc_trigger==b'ms_ck_11':
        logger.debug('recms 2')
        raw_pos = sock.recv(11)
        if not raw_pos:
            return None
        pos = pickle.loads(raw_pos)
        ms.position = pos
        ms.click(pynput.mouse.Button.left,1)
        print(ms.position)
    elif mc_trigger==b'ms_ck_12':
        logger.debug('recms 3')
        raw_pos = sock.recv(12)
        if not raw_pos:
            return None
        pos = pickle.loads(raw_pos)
        ms.position = pos
        ms.click(pynput.mouse.Button.left,1)
        print(ms.position)

        
def send_msg(sock,msg):
    raw_len= len(msg)
    len_msg=pickle.dumps(raw_len)
    sock.send(len_msg)
    sock.sendall(msg)

def Main():       
    s1=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket Created')
    port1 = 12345
    port2 = 15432
    bbox = {'top': 0, 'left': 0, 'width': 1366, 'height': 768}
    s1.bind(('',port1))
    print('socket binded to %s'%(port1))
    s1.listen()
    print("Screen Capture started")
    c, addr = s1.accept()
    print('Now connected with ',addr)
    s2.connect(('127.0.0.1',port2))
    sct = mss()
    logger.debug("Started")
    while True:
        sct_img = sct.grab(bbox)
        logger.debug("sct made")
        msg=pickle.dumps(sct_img)
        logger.debug("pickle dumped")
        send_msg(c,msg)
        logger.debug("sent")
        recms(s2)
    c.close()
    s2.close()
    pynput.mouse.Listener.stop()
    
if __name__=='__main__':
    Main()