# Import request for requesting HTTP to the server from node XYZ
import requests

# Server URL
BASE = "http://127.0.0.1:5000/"

# Get Request and concat node names 
requests.get(BASE + "nodeXYZ")
