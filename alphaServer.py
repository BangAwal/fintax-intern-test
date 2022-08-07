# Import flask for the web server
from flask import Flask 
# Import value for counting the increment value of multiple nodes
from multiprocessing import Value 

from flask_restful import abort

# Creating flask object
app = Flask(__name__)

# Instantiate counter value variable
counterABC = Value('i', 0)
counterXYZ = Value('i', 0)


# Server routing for different node
@app.route('/<string:node>')
def index(node):
    if node == "nodeABC":
        # Lock the increment value (ssh attempt) for each node everytime the get request come
        with counterABC.get_lock():
            counterABC.value += 1
            attemps = counterABC.value

        # Print the metrics on server side
        print(node + " had " + str(attemps) + " attempt(s)")

        # return success message to client, 
        # it will not shown to the client, it here only because the return is neccesary
        return {"message": "SSH success"}
    elif node == "nodeXYZ":
        with counterXYZ.get_lock():
            counterXYZ.value += 1
            attemps = counterXYZ.value       
        print(node + " had " + str(attemps) + " attempt(s)")
        return {"message": "SSH success"}
    else:
        # Abort if the nodes not valid
        abort(401, message="Nodes Invalid")

# Run flask server
if __name__ == "__main__":
    app.run(debug=True)