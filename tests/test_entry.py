import requests

# To run these tests:

# python3 -m pytest ./

# You should start the python server locally
# before starting these tests.
# To do this:
# <in the server directory>: sudo python3 server.py

def test_interface():
    URL = "http://0.0.0.0:105/hello/"
    test = requests.get(URL)
    print("Status code: {}".format(test.status_code))
    print("Text: {}".format(test.text))
    assert test.status_code == 200, "Returned status code is incorrect"
    assert test.text == "Hello World!", "Returned data / text is incorrect"