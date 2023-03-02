# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# CONG-BANG TA
# CONGBANT@UCI.EDU
# 76664422
import socket
import ds_protocol as dsp
from ds_protocol import DSPProtocolError
from collections import namedtuple

def send(server:str, port:int, username:str, password:str, message:str, bio:str=None):
  '''
  The send function joins a ds server and sends a message, bio, or both
  :param server: The ip address for the ICS 32 DS server.
  :param port: The port where the ICS 32 DS server is accepting connections.
  :param username: The user name to be assigned to the message.
  :param password: The password associated with the username.
  :param message: The message to be sent to the server.
  :param bio: Optional, a bio for the user.
  '''

  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((server, port))

    connection = init(client)
    token = join(connection, username, password)[2]

    if bio == None:
      msg = write_command(token, dsp.post(message))

    else:
      msg = write_command(token, dsp.bio(bio))

    send = client.makefile('w')
    recv = client.makefile('r')

    send.write(msg + '\r\n')
    send.flush()
    response = dsp.extract_json(recv.readline())
    print(response[1])

  pass

DSPConnection = namedtuple('DSPConnection', ['socket', 'send', 'recv'])

def init(sock: socket) -> DSPConnection:

  '''
  The init method should be called for every program that uses the SMP Protocol. The calling program should first establish a connection with a socket object, then pass that open socket to init. init will then create file objects to handle input and output.
  '''

  try:
    f_send = sock.makefile('w')
    f_recv = sock.makefile('r')
  except:
    raise DSPProtocolError("Invalid socket connection")

  return DSPConnection(socket=sock, send=f_send, recv=f_recv)

def join(dsp_conn: DSPConnection, username: str, password: str) -> str:

  '''
  Sends a join command to server and checks if it was successful
  :param dsp_conn:
  :param username:
  :param password:
  :return:
  '''

  try:
    write_join(dsp_conn, username, password)
    response = checkJoin(dsp_conn)
    return response
  except:
    raise DSPProtocolError

def disconnect(dsp_conn: DSPConnection):

  '''
  Disconnects from the server
  :param dsp_conn:
  :return:
  '''

  dsp_conn.send.close()
  dsp_conn.recv.close()

def write_join(dsp_conn: DSPConnection, usr, pwd):

  '''
  Writes the join command that will be sent
  :param dsp_conn:
  :param usr:
  :param pwd:
  :return:
  '''

  try:
    cmd = dsp.join(usr, pwd)
    dsp_conn.send.write(cmd + '\r\n')
    dsp_conn.send.flush()
  except:
    raise DSPProtocolError

def write_command(token: str, content: str):

  '''
  Writes the other commands that wil be sent
  :param token:
  :param content:
  :return:
  '''

  try:
    cmd = '{{"token": "{token}", {content}}}}}'.format(token = token, content = content)
    return cmd
  except:
    raise DSPProtocolError

def checkJoin(dsp_conn: DSPConnection) -> str:
  result = dsp.check_join(dsp_conn.recv.readline())
  return result