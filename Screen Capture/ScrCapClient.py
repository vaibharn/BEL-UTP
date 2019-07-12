
from mss import mss
from multiprocessing.connection import Client

address = ('localhost', 6000)
conn = Client(address, authkey=b'password')
print("Screen Capture started")
while(True):
    bbox = {'top': 0, 'left': 0, 'width': 800, 'height': 600}
    sct = mss()
    while True:
        sct_img = sct.grab(bbox)
        conn.send(sct_img)
        
conn.send('close')
conn.close()

