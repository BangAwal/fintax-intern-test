# Import flask for the web server
from flask import Flask 
# Import value for counting the increment value of multiple nodes
from multiprocessing import Value 

# Creating flask object
app = Flask(__name__)

# Server routing for different node
@app.route('/<string:node>')
def index(node):
    if node == "nodeABC":
        return {"node": node}
    else:
        return {"node": node}


# Run flask server
if __name__ == "__main__":
    app.run(debug=True)