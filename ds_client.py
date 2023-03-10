# Starter code for assignment 3 in ICS 32 Programming with Software Libraries
# in Python

# Replace the following placeholders with your information.

# Benjoseph Villamor
# villamob@uci.edu
# 62443909

import socket
import ds_protocol
import json


def send(server: str, port: int, username: str, password: str, message: str, bio: str = None):
    '''
    The send function joins a ds server and sends a message, bio, or both

    :param server: The ip address for the ICS 32 DS server.
    :param port: The port where the ICS 32 DS server is accepting connections.
    :param username: The user name to be assigned to the message.
    :param password: The password associated with the username.
    :param message: The message to be sent to the server.
    :param bio: Optional, a bio for the user.
    '''
    bool = True
    # Attempt to connect to the server
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((server, port))
        print(f'connected to {server} on {port}')
    # catches server connection error
    except socket.gaierror:
        print('Issue connecting with server.')
        bool = False
    # catches port connection error
    except TimeoutError:
        print('Issue connecting with port.')
        bool = False
    # catches ip connection error
    except ConnectionRefusedError:
        print('Issue connecting with ip.')
        bool = False
    # catches type error for server, port, username, and password parameters
    except TypeError:
        if type(server) != str:
            bool = False
            print('Incorrect server type.')
        if type(port) != int:
            bool = False
            print('Incorrect port type.')
        if type(username) != str:
            bool = False
            print('Incorrect user type.')
        if type(password) != str:
            bool = False
            print('Incorrect password type.')

    # checks if an error has been made
    if bool:
        # sends message to server following DSP protocol
        # receives response from server
        join_msg = ds_protocol.join(username, password)
        client.sendall(join_msg.encode())
        received_join = client.recv(4096).decode()
        join_dict = json.loads(received_join)
        print(received_join)
        try:
            extract = ds_protocol.extract_json(received_join)
            token = extract.token
        except KeyError:
            bool = False
            print(join_dict['response']['message'])
        except UnboundLocalError:
            bool = False
            print('Unable to extract data.')
    else:
        pass

    # checks if message and bio are viable types
    if bool:
        if type(message) == str or message is None:
            pass
        else:
            bool = False
            print('Incorrect message type.')
        if type(bio) == str or bio is None:
            pass
        else:
            print(type(bio))
            bool = False
            print('Incorrect bio type.')

    if bool:
        # sends message if no error was found
        if message is not None:
            if message == '' or message.isspace():
                bool = False
                print('Post is invalid')
            else:
                if extract.response['type'] == 'ok':
                    post_format = ds_protocol.post(token, message)
                    client.sendall(post_format.encode())
                    received_post = client.recv(4096).decode()
                    print(received_post)
                else:
                    bool = False
                    print('Error publishing post to server')

        # sends bio if no error was found
        count = 1
        if bio is not None:
            if message is not None and (message == '' or message.isspace()):
                bool = False
                count -= 1
            elif (bio == '' or bio.isspace()) and count == 1:
                pass
            else:
                if extract.response['type'] == 'ok':
                    bio_format = ds_protocol.bio(token, bio)
                    client.sendall(bio_format.encode())
                    received_bio = client.recv(4096).decode()
                    print(received_bio)
                else:
                    bool = False
                    print('Error publishing bio to server')
    else:
        pass

    return bool
