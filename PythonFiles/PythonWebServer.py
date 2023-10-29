import http.server
import socketserver
import ssl
import os

Path = os.path.dirname(__file__)

def encrypt():

    clear_file = Path + "/payloadClear.txt"
    encrypted_file = Path + "/payloadEncrypted.txt"

    with open(clear_file, 'r') as input_file:
        file_contents = input_file.read()

    ##file_contents = file_contents.replace('"','').replace("\n","")

    key = 'K'  # Any character will work
    output = list(file_contents)
    
    for i in range(len(file_contents)):
        output[i] = chr(ord(file_contents[i]) ^ ord(key))
    
    with open(encrypted_file, 'w',encoding="utf-8") as output_file:
        output_file.write(''.join(output))

def Server(ip,port):

    handler = http.server.CGIHTTPRequestHandler

    # Create an SSL context
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile=Path + '/mycert.pem', keyfile=Path + '/mykey.key')

    httpd = socketserver.TCPServer((ip, port), handler)
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

    print(f"Server started on https://{ip}:{port}")
    httpd.serve_forever()

def RunServer():
    try:
        Server("127.0.0.1",9000)
    except KeyboardInterrupt:
        print("\nServer Stopped")

if __name__ == "__main__":
    encrypt()
    RunServer() 

