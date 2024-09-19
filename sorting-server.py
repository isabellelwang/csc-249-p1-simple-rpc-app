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
            number_list = data.split(" ")
            number_list = [item.lower() for item in number_list]

            if "ascending" in number_list: 
                number_list.remove("ascending")
                number_list.sort(key=int)
                print(number_list)
            elif "descending" in number_list: 
                number_list.remove("descending")
                number_list.sort(key=int, reverse = True)
            else: 
                print("Invalid Operation. Please Try Again.")
            
            conn.sendall(bytes(str(number_list), 'utf-8'))


print ("server is done!")