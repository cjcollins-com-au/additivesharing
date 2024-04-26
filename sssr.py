import socket
import time

chunkSize = 1024

# Simple Socket Send and Receive functions
# Simple functionality only for sending and receiving data for simple exchange
# By design we only exchange 1K at a time :)

# designed for sending simple messages only
def send_socket_data(dest_sock_ip, dest_sock_port, msg):
    return_val = "NOK"

    # TCP/IPv4 type socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.settimeout(30)

    # establish connection - we'll allow 30 seconds...
    # (in a loop, the timeout value above doesn't work for completely
    # non-existent connections)

    attempt_counter = 0
    got_connect = True
    while True:
        attempt_counter += 1
        try:
            sock.connect((dest_sock_ip, dest_sock_port))
            break
        except:
            print(".", end="", flush=True)

            if attempt_counter > 30:
                got_connect = False
                break
            else:
                time.sleep(1)

    if not got_connect:
        print("Could not connect to other party")
        return

    msg = str(msg)

    # get data
    while True:
        for i in range(0, len(msg), chunkSize):
            sock.send(msg[i:i+chunkSize].encode('utf-8'))

            response = sock.recv(1024)
            response = response.decode("utf-8")

            # check other party got message ok
            if response == "OK":
                return_val = response
            if response == "":
                break

        # send end message
        sock.send("END".encode("utf-8"))
        response = sock.recv(1024)
        response = response.decode("utf-8")
        if response != "ENDED":
            return_val = response = response
        break

    sock.close()
    return return_val


# Receiving simple messages only
# reads in 1024 byte chunks, expects "END" ... to end
def get_socket_data(sock_ip, sock_port):
    # return data
    return_string = ""

    #TCP/IPv4 type socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.settimeout(30)
    sock.bind((sock_ip, sock_port))

    # listen - 1 client
    sock.listen(0)
    print("Waiting for a connection... ", end = "")

    # accept connections
    client_port, client_ip = sock.accept()
    print("Got connection... ")

    # get data
    while True:
        req_data = client_port.recv(chunkSize)
        req_data = req_data.decode("utf-8")

        if req_data == "END":
            client_port.send("ENDED".encode("utf-8"))
            break
        if req_data == "":
            break
        else:
            return_string += req_data

            client_port.send("OK".encode("utf-8"))

        #print("Request received:", req_data)

    client_port.close()
    sock.close()

    return return_string
