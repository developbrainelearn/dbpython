import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('127.0.0.1',8888))
s.listen(3)
print('Waiting for client...')

while True:
    client, address = s.accept()
    client.send(bytes('Welcome to developBrain\nWhat is your name ?','utf-8'))
    name = client.recv(1024)
    print('Connection with',name.decode('utf-8'),address)

    while True:
        write = input('>>')
        send_msg = client.send(bytes(write,'utf-8'))
        rec_msg = client.recv(1024)
        print(rec_msg.decode('utf-8'))

        if write == 'Thank you':
            client.close()
            exit(0)
