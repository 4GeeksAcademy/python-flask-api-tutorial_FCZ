from flask import Flask
from flask import request
app = Flask(__name__)

todos = [ { "label": "My first task", "done": False } ]

@app.route('/myroute', methods=['GET'])
def hello_world():
    return 'Hello World!'


@app.route('/todos', methods=['GET'])
def get_todos():
    return todos

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return todos

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    todos.pop(position)
    return todos



# Estas dos líneas siempre deben estar al final de tu archivo app.py

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)