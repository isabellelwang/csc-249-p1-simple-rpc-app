import socket 

HOST = "127.0.0.1"
PORT = 65432

print("client starting - connecting to server at IP", HOST, "and port", PORT)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
    s.connect((HOST,PORT))
    print(f"connection established")
    print(f"------- Sorting Numerical Dataset ---------")
    while True: 
        #print("Please type in the kind of sorting you want to perform along with a list of numbers: \n Ascending \n Descending")
        MSG = input("Please type in the kind of sorting you want to perform along with a list of numbers: \n Ascending \n Descending\n")
        if not MSG: 
            break 
        print(f"Sending message... '{MSG}'")
        s.sendall(bytes(MSG, 'utf-8'))
        print('message sent, waiting for reply"')