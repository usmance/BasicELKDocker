# Python lib for docker engine.
import sys
import docker
import threading


def HealthCheck():
   
        client = docker.from_env()
        x=client.containers.list(all='true')
        #Looping through all containers.
        for i in range(len(x)):
            statusCheck=x[i].status

            #Health check criteria is checking if the container is running 
            # and if the container is running , run a command in that container.
            if statusCheck=='running':
                y=x[i].exec_run("echo XYZ")
                if y[0]==0:
                    print('Container --'+x[i].short_id+' in good health. Will check again after 15 min.')
                    print(" ")
            else:
                x[i].start()
                print('Starting container --'+ x[i].short_id+' again..')
                print(x[i].status)
 

def setInterval(func,time):
    e=threading.Event()
    while not e.wait(time):
        func()

if __name__ == "__main__":

    # intervalTime=int(sys.argv[1])

    intervalTime=5
    setInterval(HealthCheck,intervalTime)