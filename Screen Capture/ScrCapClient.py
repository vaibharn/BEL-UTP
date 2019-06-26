
from mss import mss
from multiprocessing.connection import Client

address = ('localhost', 6000)
conn = Client(address, authkey=b'secret password')
while(True):
    print("producer")
    bbox = {'top': 100, 'left': 0, 'width': 400, 'height': 300}
    sct = mss()
    while 1:
        sct_img = sct.grab(bbox)
        conn.send(sct_img)
        
conn.send('close')
conn.close()

