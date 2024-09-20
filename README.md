RPC Numerical List Sorting RPC Client-Server App
Name: Isabelle Wang

Instructions: 
## Deliverables

Your work on this project must be submitted for grading by **Friday, September 20th at 11:59PM**. Extensions may be obtained by sending me a message on Slack before the original due date.

All work must be submitted in Gradescope.

You must submit these work products:

1. Source code for your client and server. Ideally, this will be a link to your public Git code repo. (Use of Git is encouraged but not required; you may instead upload your individual Python files directly to Gradescope without involving Git.)
2. A document with a written description of your client-server message format (that is, a description of all implemented client and server messages, and how the various components of each message are represented). This document must also briefly summarize what your client-server application does, and provide examples of expected output for all implemented RPC operations. Your goal in writing this document should be to convey enough information in enough detail to allow a competent programmer **without access to your source code** to write either a new client that communicates properly with your server, or a new server that communicates properly with your client. This document should include at least five sections: Overview of Application, Client->Server Message Format, Server->Client Message Format, Example Output, Acknowledgments.
3. A command-line trace showing the client and server in operation. 


Overview of Application: 





EXAMPLE: Ascending 12 3 31 2 0 321

Server --> Client Message Format
server starting - listening for connections at IP
Server is binding to Host and Port
Listening for incoming connections...
Connection Accepted.
Connected established with ('127.0.0.1', 52049)
Received client message: 'b'Ascending 12 3 31 2 0 321'' [25 bytes]
requested sorting operation is ascending
server is done!

Client --> Server Message Format 
client starting - connecting to server at IP 127.0.0.1 and port 65432
connection established
------- Sorting Numerical Dataset ---------
Please type in the kind of sorting you want to perform AND the list of numbers to sort: 
-Ascending 
-Descending
-Enter to exit
Ascending 12 3 31 2 0 321
Sending message... 'Ascending 12 3 31 2 0 321'
message sent, waiting for reply"
Received server message: 'b"['0', '2', '3', '12', '31', '321']"' [34 bytes]
client is done!

Example output: 
Descending 

SERVER 
client starting - connecting to server at IP 127.0.0.1 and port 65432
Server is binding to Host and Port
Listening for incoming connections...
Connection Accepted.
Connected established with ('127.0.0.1', 52076)
Received client message: 'b'Descending 12 32 3 124 5 2 1'' [28 bytes]
requested sorting operation is descending
request includes  7  arguments: ['12', '32', '3', '124', '5', '2', '1']
sending result back to client:  ['124', '32', '12', '5', '3', '2', '1']
server is done!

CLIENT
client starting - connecting to server at IP 127.0.0.1 and port 65432
connection established
------- Sorting Numerical Dataset ---------
Please type in the kind of sorting you want to perform AND the list of numbers to sort: 
-Ascending 
-Descending
-Enter to exit
Descending 12 32 3 124 5 2 1
Sending message... 'Descending 12 32 3 124 5 2 1'
message sent, waiting for reply"
Received server message: 'b"['124', '32', '12', '5', '3', '2', '1']"' [39 bytes]
client is done!

Acknowledgments: 
