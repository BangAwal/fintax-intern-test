# Import flask for the web server
from flask import Flask 
# Import value for counting the increment value of multiple nodes
from multiprocessing import Value 

# Creating flask object
app = Flask(__name__)

# Run flask server
if __name__ == "__main__":
    app.run(debug=True)