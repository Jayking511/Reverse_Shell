# Reverse_Shell

This project creates a ***REMOTE SHELL*** between the server and clients.

If server wants to connect with the client, there will be a lot of things that prevents the connection. But here, the client initiates the connection to server. So, this simplifies the process of establishing the connection.

The server can handle multiple connections from multiple clients at a same time and manage to shift among the clients.

Initial interface of the server will be as follows:

![image](https://user-images.githubusercontent.com/92370004/194110073-586ab7db-da20-45c7-bd55-52a0fb981197.png)

Main Menu will contain following options:

. list    - List all avilable connections

. select  - Select the connection using index provided in the list

. exit    - Exit from the program

Interface when connected to shell will be as follows:

![image](https://user-images.githubusercontent.com/92370004/194110924-5ca5dfaf-012c-4919-82dd-ab152c51b77e.png)

User can type in the commands for the client and results for the commands will be received in server.

Exit options for client are:

. exit  - Exits from the remote shell, but the connection will be alive

. quit  - Exits from the shell and closes the connection between the server and the client.
