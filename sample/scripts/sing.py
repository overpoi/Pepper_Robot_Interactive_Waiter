import sys
import time
import os

try:
    sys.path.insert(0, os.getenv('MODIM_HOME')+'/src/GUI')
except Exception as e:
    print "Please set MODIM_HOME environment variable to MODIM folder."
    print e
    sys.exit(1)

import ws_client
from ws_client import *


def sing1():

    im.setProfile(['*', '*', 'it', '*'])

    im.execute('song1')
    time.sleep(3)
    im.execute('song2')        

    

if __name__ == "__main__":

    cmdsever_ip = '127.0.0.1'
    cmdserver_port = 9101
    demo_ip = '127.0.0.1'
    demo_port = 8000

    mws = ModimWSClient()
    # local execution
    mws.setDemoPathAuto(__file__)

    mws.run_interaction(sing1)


