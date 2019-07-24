# -*- coding: utf-8 -*-

import socket 
from mss import mss
import pickle


def send_msg(sock,msg):
    raw_len= len(msg)
    len_msg=pickle.dumps(raw_len)
    sock.send(len_msg)
    sock.sendall(msg)

def Main():   
    s=socket.socket()
    print('Socket Created')
    port = 12345
    bbox = {'top': 0, 'left': 0, 'width': 1366, 'height': 768}
    s.bind(('',port))
    print('socket binded to %s'%(port))
    s.listen()
    
    print("Screen Capture started")
    c, addr = s.accept()
    print('Now connected with ',addr)
    sct = mss()
    while True:
        sct_img = sct.grab(bbox)
        msg=pickle.dumps(sct_img)
        send_msg(c,msg)
    c.close()

if __name__=='__main__':
    Main()