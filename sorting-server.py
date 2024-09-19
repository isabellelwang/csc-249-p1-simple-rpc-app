import socket 

HOST = "127.0.0.1"
PORT = 65432

print("server starting - listening for connections at IP")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
    s.bind((HOST, PORT))
    s.listen() 
    conn, addr = s.accept()

    with conn: 
        print(f"Connected established with {addr}")
        while True: 
            data = conn.recv(1024)
            if not data: 
                break 
            print (f"Received client message: '{data!r}' [{len(data)} bytes]")
            conn.sendall(data) 

print ("server is done!")