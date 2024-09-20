## Project: RPC Numerical List Sorting RPC Client-Server App
## Name: Isabelle Wang 

## Deliverables

## -----------Section1: Overview of Application------------

The Sorting RPC Client-Server App has two files-- sorting-client.py and sorting-server.py. In the sorting client.py, there is a user input from the keyboard for two operations: Ascending and Descending, along with a list of numbers (floats). 

First, the sockets are the user the prompted to type in a command in the keyboard: Ascending/Descending followed by a list of numbers (e.g. Ascending 1 2 31.2 34 4121.2). Then this message is encoded in utf-8 and sent to the server. The server receives the message and decodes it. Then the data is converted into a string so it split each component of the message by a space " " into a list. The program will make a new list but lowercase each string value to handle case sensitivity/capitalization errors. 

Afterwards, the program will search for the command ("ascending/descending") in the list to provide the requested computation. Then it takes the list of string numbers and sorts it as floats. If the ascending and descending command is correctly spelled, then a new variable response will store the sorted list of numbers. Otherwise, the response variable will store "Invalid Operation/Spelling", to prevent program crashes. The sorted list is encoded again and sent back to the client. 

## ------------Section2: Client--> Server Message Format-----------
sorting-client.py uses a TCP socket and connects to a host and port. It also has a function called encode which takes in a socket and the message input and encodes it, so that it could be sent to the server. The message is a string, but the list of numbers will be sorted as floats. Then, it also waits for a processed response from the server. 


## -----------Section3: Server->Client Message Format-----------
sorting-server.py also uses a TCP socket to listen and accept a connection from the client. It receives the command message from the server and processes the information into a function called decode. 

The decode function takes in the message and socket as parameters. It decodes the message and changes it into a string. Then it splits the data by whitespaces and creates a new list with each string value lowercased. This is to handle inconsistent letter case. Using the lower case list, the function searches for the command and performs the sorting operation based on the command. 

To handle spelling errors or wrong commands, the program will send the response as "Invalid response" and prevent the program from crashing. After sorting, the response is encoded and sent back to the client. 

## ---------Section4: Example output with Command Line Trace ---------

### ---------Ascending---------
#### Server --> Client Message Trace

python sorting-server.py

client starting - connecting to server at IP 127.0.0.1 and port 65432

Server is binding to Host and Port

Listening for incoming connections...

Connected established with ('127.0.0.1', 49776)

Message received! 'b'Ascending 12.2 3 23 1.3 2''

Received client message: 'b'Ascending 12.2 3 23 1.3 2'' [25 bytes]

requested sorting operation is ascending

request includes  5  arguments: ['12.2', '3', '23', '1.3', '2']

sending result back to client:  ['1.3', '2', '3', '12.2', '23']

server is done!


#### Client --> Server Message Trace

python sorting-client.py

client starting - connecting to server at IP 127.0.0.1 and port 65432

connection established

------- Sorting Numerical Dataset ---------

Please type in the kind of sorting you want to perform AND the list of numbers to sort: 

-Ascending 

-Descending

-Enter to exit

Ascending 12.2 3 23 1.3 2

Sending message... 'Ascending 12.2 3 23 1.3 2'

message sent, waiting for reply"

Received server message: 'b"['1.3', '2', '3', '12.2', '23']"' [31 bytes]

client is done!



### ------Descending-------- 

#### Server --> Client Message Trace

python sorting-server.py

client starting - connecting to server at IP 127.0.0.1 and port 65432

Server is binding to Host and Port

Listening for incoming connections...

Connected established with ('127.0.0.1', 49783)

Message received! 'b'Descending 12.4 2 432.1 4''

Received client message: 'b'Descending 12.4 2 432.1 4'' [25 bytes]

requested sorting operation is descending

request includes  4  arguments: ['12.4', '2', '432.1', '4']

sending result back to client:  ['432.1', '12.4', '4', '2']

server is done!

#### Client --> Server Message Trace

python sorting-client.py

client starting - connecting to server at IP 127.0.0.1 and port 65432

connection established

------- Sorting Numerical Dataset ---------

Please type in the kind of sorting you want to perform AND the list of numbers to sort: 

-Ascending 

-Descending

-Enter to exit

Descending 12.4 2 432.1 4

Sending message... 'Descending 12.4 2 432.1 4'

message sent, waiting for reply"

Received server message: 'b"['432.1', '12.4', '4', '2']"' [27 bytes]

client is done!


### -------ERROR HANDLING (Incorrect Spelling)-----------
#### Server --> Client Message Trace

python sorting-server.py

client starting - connecting to server at IP 127.0.0.1 and port 65432

Server is binding to Host and Port

Listening for incoming connections...

Connected established with ('127.0.0.1', 49787)

Message received! 'b'Acnddg 1 24 42.2 2''

Received client message: 'b'Acnddg 1 24 42.2 2'' [18 bytes]

Invalid Operation/Spelling. Try Again.

sending result back to client:  Invalid Operation/Spelling.

server is done!


#### Client --> Server Message Trace

python sorting-client.py

client starting - connecting to server at IP 127.0.0.1 and port 65432

connection established

------- Sorting Numerical Dataset ---------

Please type in the kind of sorting you want to perform AND the list of numbers to sort: 

-Ascending 

-Descending

-Enter to exit

Acnddg 1 24 42.2 2

Sending message... 'Acnddg 1 24 42.2 2'

message sent, waiting for reply"

Received server message: 'b'Invalid Operation/Spelling.'' [27 bytes]

client is done!


## ---------Section5: Acknowledgments------------
Thank you to Quinn sharing their understanding of the instructions of designing a method for encoding/decoding client requests. 