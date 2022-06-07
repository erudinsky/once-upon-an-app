from flask import Flask
import socket

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
  return 'Hello world!'

@app.route('/ping', methods=['GET'])

def ping():
  return f'Pong from {socket.getfqdn()}'

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')
  
def codesmell():
  return 1<>1
