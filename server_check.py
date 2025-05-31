import socket

def is_server_avalible(host ,port):
    try:
        with socket.create_connection((host ,port), timeout =3):
            return True
    except OSError :
        return False

if is_server_avalible("google.com",80):
    print("server is reachable")
else:
     print("server is reachable")
