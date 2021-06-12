from flask import Flask

# Create the server app
app = Flask(__name__)


# Define what happens when the user performs
# a GET request on the hello endpoint
# Sample use
# curl -X GET http://0.0.0.0:105/hello/
@app.route('/hello/', methods=['GET'])
def welcome():
    return "Hello World!"


# Entry point
if __name__ == '__main__':
    print("Starting the REST server")
    app.run(host='0.0.0.0', port=105)
