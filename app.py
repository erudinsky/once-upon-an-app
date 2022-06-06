from flask import Flask
import socket

app = Flask(__name__)

@app.route('/ping', methods=['GET'])

def ping():
  return f'Pong from {socket.getfqdn()}'

if __name__ == "__main__":
  app.run(debug=True)