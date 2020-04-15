# Python lib for docker engine.
import sys
import docker
import threading
from random import randint

def removeRandomContainer():
    client = docker.from_env()

    #Getting all running containers from docker daemon.
    containerList=client.containers.list()  
    
    

    containerRemoved=0
    
    while containerRemoved!=1:
        
        #Selecting a random index between len(containerList)
        randomContaniner=randint(0,len(containerList)-1)
        if containerList[randomContaniner].status=='running':
            print(containerList[randomContaniner],' Stoped')
            

            #Stopping that random container,
            containerList[randomContaniner].stop()
            containerList[randomContaniner].remove()
            print('Container removed.')
            containerRemoved=1

                
if __name__ == "__main__":
    removeRandomContainer()