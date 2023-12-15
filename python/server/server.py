"""
Module: server

This module classes for a basic TCP Server

Author: Nicholas Ong

Classes:
  - TCPServer: Base class for a TCP Server
"""

import socket

HOST = "127.0.0.1"
PORT = 5000

class TCPServer:
  """
  TCPServer is an implementation of a TCP Server in Python

  Attributes:
    host (str): IP address of socket
    port (int): Port number of socket
    server_socket (socket.socket): socket

  Methods:
    start: start the server
    close: close the server
    handle_request: internal method to receive client request
  """
  def __init__(self, host, port):
    self.host = host
    self.port = port
    self.server_socket = None

  def start(self):
    """
    Starts the TCP server.

    Parameters:
      None

    Returns:
      None

    Example:
      server = TCPServer(host, port)
      server.start()
    """
    self.server_socket = socket.socket(
      family=socket.AF_INET,
      type=socket.SOCK_STREAM
    )

    self.server_socket.setsockopt(
      socket.SOL_SOCKET,
      socket.SO_REUSEADDR,
      1
    )

    self.server_socket.bind((self.host, self.port))
    self.server_socket.listen(5)

    print(f"Socket listening on http://{self.host}:{self.port}")
    try:
      while True:
        client_socket, client_address = self.server_socket.accept()
        print("Connected by", client_address)
        data = client_socket.recv(1024)

        response = self.handle_request(data)
        print(response)

        client_socket.sendall(response)
        client_socket.close()
    finally:
      self.server_socket.close()


  def close(self):
    """
    Closes an already running TCP Server.

    Parameters:
      None

    Returns:
      None

    Example:
      server = TCPServer(host, port)
      server.start()
      server.close()
    """
    print("closing socket")
    self.server_socket.close()


  def handle_request(self, data):
    """
    Handles request data from client sockets

    Parameters:
      data (bytes): data given by the client socket

    Returns:
      bytes: bytes retrieved from socket

    Example:
      response = self.handle_request(data)
    """
    return data


if __name__ == "__main__":
  server = TCPServer(HOST, PORT)
  server.start()
