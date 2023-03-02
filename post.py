import requests
import os
import socket
import threading
import time

device = os.environ["COMPUTERNAME"]
room = socket.gethostbyname(socket.gethostname())
url = 'http://localhost:5000/add?name={}&room={}'.format(str(device), str(room))

x = requests.post(url)

print(x.text)

def get_state(): 
    request = requests.get('http://localhost:5000/ping')
    return request.text
    
def threadFunc():
    resp = (get_state()).strip("{}")
    if resp == "true":
        print("Running")
    # by only providing an if statement above, we stop the possibility of an unwanted accident
    print("attack? " + resp)
    time.sleep(1)
    threadFunc()
            
def run():
    pass
    
if __name__ == "__main__": 
    ping_thread = threading.Thread(target=threadFunc, daemon=True)
    ping_thread.start()
    while True: time.sleep(1000)
