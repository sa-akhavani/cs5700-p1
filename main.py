import socket
import ssl
import sys

def solve_operation(a, op, b):
    if op == '+':
        return int(a) + int(b)
    elif op == '-':
        return int(a) - int(b)
    elif op == '/':
        return int((int(a) / int(b)))
    elif op == '*':
        return int(a) * int(b)
    else:
        print('Error!')

    
def handle_operation(str):
    splitted = str.split()
    a = splitted[2]
    op = splitted[3]
    b = splitted[4]
    return a, op, b

def handle_bye(str):
    splitted = str.split()
    return splitted[1]

def identify_message_type(str):
    splitted = str.split()
    if splitted[1] == 'STATUS':
        return 'status'
    else:
        return 'bye'

def handle_args(all_args):
    if len(all_args) < 3:
        print('Invalid Arguments')
        exit()

    is_ssl = False
    port = 27995
    index = 1

    if '-s' in all_args:
        is_ssl = True
        port = 27996
        index += 1

    if '-p' in all_args:
        port = int(all_args[all_args.index('-p') + 1])
        index += 2

    if not index >= len(all_args) - 1:
        hostname = all_args[index]
        neu_id = all_args[index+1]
    else:
        print('Invalid Arguments')
        exit()
    
    return hostname, port, neu_id, is_ssl



# Parse Args
hostname, port, neu_id, is_ssl = handle_args(sys.argv)

# Create Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #ipv4, tcp

# Wrap The Socket Around SSL
if is_ssl:
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.check_hostname = 0
    context.verify_mode = 0
    if is_ssl:
        wrapped_sock = context.wrap_socket(sock, server_hostname=hostname)
        sock = wrapped_sock

# Connect
sock.connect((hostname, port))

#Send Hello
HELLO_MESSAGE = 'cs5700fall2020 HELLO ' + neu_id + '\n'
sock.send(HELLO_MESSAGE.encode())

# Main logic
bye = 0
while bye == 0:
    server_msg = sock.recv(256)
    if(server_msg):
        server_msg = server_msg.decode()

        msg_type = identify_message_type(server_msg)
        if (msg_type == 'status'):
            a, op, b = handle_operation(server_msg)
            result = solve_operation(a, op, b)
            sock.send(('cs5700fall2020 ' + str(result) + '\n').encode())
        elif (msg_type == 'bye'):
            secret_flag = handle_bye(server_msg)
            print(secret_flag)
            bye = 1
        else:
            print('Error in message type: ', msg_type)
    else:
        break

sock.close()
