__author__ = 'frealgagu'

from bomberkiller import BomberKiller
from sys import argv
from time import sleep

if __name__ == "__main__":

    host = None
    port = None
    username = None
    token = None
    number = -1

    if len(argv) > 4:
        host = argv[1]
        port = int(argv[2])
        username = argv[3]
        token = argv[4]
    else:
        host = "172.16.0.3"
        host = "192.168.243.245"
        port = 5000
        number = 0
        if number == 0:
            username = "BomberKiller"
            token = "532c9405cffad45921000001"
        elif number == 1:
            username = "uno"
            token = "5333750c32b53dac05000003"
        elif number == 2:
            username = "dos"
            token = "533376ed32b53dac05000017"
        elif number == 3:
            username = "tres"
            token = "5333773c32b53dac05000027"
        elif number == 4:
            username = "cuatro"
            token = "5333777832b53dac05000032"
        elif number == 5:
            username = "frealgagu"
            token = "5340d6f7ef66227907000228"

    while True:
        bomberKiller = BomberKiller(host, port, username, token)
        bomberKiller.run()
        print "Esperando 5 segundos para volver a empezar..."
        sleep(5)
        print "Empezando de nuevo."