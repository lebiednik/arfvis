import socket
import json
import struct
import urllib.request
import sys

def sendInfo(djangoSocket, message):
    try:
        request = urllib.request.Request(url='http://' + djangoSocket + '/rfvisapp/',
            data=json.dumps(message).encode('utf8'),
            method='PUT',
            headers={'content-type':'application=json'})
    except:
        print(type(djangoSocket))
        print(type(data))
        print(type(method))
        print(type(headers))
    with urllib.request.urlopen(request) as f:
        pass
    print(f.status)
    print(f.reason)

def main(argv):
    print ("Arg: " )
    print (argv)
    if (len(argv) == 2):
        djangoSocket = argv[1]
    else:
        djangoSocket = 'localhost:8000'
    listenSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


    host = '192.168.1.255'
    port = 8702

    #buffer_size = 4096
    listenSocket.bind(('', port))


    print("Listening on %s:%s..." % (host, str(port)))
    try:
        while True:
            data, addr = listenSocket.recvfrom(1024)
            message = json.loads(data)
            print(message)
            sendInfo(djangoSocket, message)

    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main(sys.argv)
"""
def main(argv):
    #get wifi device from argv
    print ("Arg: " )
    print (argv)
    if (len(argv) == 3):
        interface = argv[1]
        socket = argv[2]
    else:
        interface = 'wlp3s0'
        socket = 'localhost:8000'
    #while(1):
    #Get GPS Coords
    #perform scan
    #send scan results
    while (1):
        wifitree = scan('wlp3s0')
        sendSignals(socket, wifitree)
        time.sleep(10) #wait 10 seconds, then rescan

if __name__ == "__main__":
    main(sys.argv)
"""
