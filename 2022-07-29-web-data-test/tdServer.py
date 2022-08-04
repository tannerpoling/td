import socket
import pickle
import threading
import numpy as np
import queue

debug = False

# server code made to run in .td file, accept local connection, 
# and update a table DAT with incoming data

# recieves data from client, then stores in a queue that is contained in
# whatever 


server_address = '10.0.0.4'
server_port = 7000
output_table_dat = "serverTable"
# note: better to have server address, port, table DAT name in an external config file
# to be accessed by both server and client file (only change in one place). 
# would be cool to have touchdesigner access cfg file for tableDAT name as well


def server_thread():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((server_address, server_port))
    s.listen(5)

    print('server start!')

    while True:
        clientsocket, address = s.accept()
        print("Connection from: " + str(address))

        # send success message to client
        msg = "successful conncection!"
        clientsocket.send(bytes(msg, "utf-8"))
	
    # now recieve data from client
        while True:
            data = clientsocket.recv(4096)
            try:
                data_decode = pickle.loads(data)
                if debug:
                	print(str(data_decode))
                	print('synth1: ' + str(data_decode[:,0]))
                myInQ.put(data_decode)
                # for i in range(data_decode.shape[0]):
                #     for j in range(data_decode.shape[1]):
                #         n[i+1, j+1] = data_decode[i][j]
            except EOFError:
                clientsocket.close()

n = op(output_table_dat)

n.setSize(5, 5)
n.replaceRow(0, [None, 'synth0', 'synth1', 'synth2', 'synth3'])
n.replaceCol(0, [None, 'freq', 'gain', 'mod', 'enable'])

myInQ = queue.Queue()
me.parent().store('inQ', myInQ)
me.parent().storeStartupValue('inQ', None) 

mainthread = threading.Thread(target=server_thread, args=())
mainthread.start()
