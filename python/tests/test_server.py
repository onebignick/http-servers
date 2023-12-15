import unittest
import socket
import threading
import time
from server.server import TCPServer

class TestTCPServer(unittest.TestCase):
    """
    class to test TCP Server
    """
    def setUp(self):
        """
        set up TCP Server for testing
        """
        self.server = TCPServer("localhost", 8888)
        self.server_thread = threading.Thread(target=self.server.start)
        self.server_thread.start()
        
        # Wait for the server to start
        time.sleep(0.1)


    def tearDown(self):
        """
        tear down TCP Server after testing
        """
        self.server.close()
        try:
            self.server_thread.join(timeout=10)
        except Exception as e:
            print(f"Error in tearDown: {e}")

    
    def test_handle_request_1(self):
        """
        Test 1: Client sends valid data
        """
        client_socket = socket.socket(
            family=socket.AF_INET,
            type=socket.SOCK_STREAM
        )

        client_socket.connect(("localhost", 8888))

        request_data = b"Hello World!"
        client_socket.sendall(request_data)
        
        # Receive the response
        response = client_socket.recv(1024)

        # Assert that the response matches the expected result
        self.assertEqual(response, request_data)

        client_socket.close()


if __name__ == "__main__":
    unittest.main()
