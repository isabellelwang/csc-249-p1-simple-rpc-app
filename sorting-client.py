import socket 

HOST = "127.0.0.1" #Host addres
PORT = 65432 #Port number 

def encode_message(MSG, so): 
    '''
    Encodes message from keyboard input and sends it to the server. Then waits for response, and prints the response with corresponding bytes. 

    param: MSG: data from client
    so: socket
    '''

    print(f"Sending message... '{MSG}'")
    so.sendall(bytes(MSG, 'utf-8')) #send the message to the server 
    print('message sent, waiting for reply"')
    response = so.recv(1024) # Receives the response with the computations applied 
    print (f"Received server message: '{response!r}' [{len(response)} bytes]")

    return response 
        
def main(): 
    print("client starting - connecting to server at IP", HOST, "and port", PORT)

    #create a TCP Socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
        s.connect((HOST,PORT)) #connect socket to host and port
        print(f"connection established")
        print(f"------- Sorting Numerical Dataset ---------")
        #ask user for input from keyboard. 
        MSG = input("Please type in the kind of sorting you want to perform AND the list of numbers to sort: \n-Ascending \n-Descending\n-Enter to exit\n")
        final_response = encode_message(MSG, s) #encode and send the message 

    print(f"client is done!")

if __name__ == "__main__": 
    main()

    