# Zendesk Ticket Viewer
_Part of the 2018 Zendesk Summer Internship Interview_

# Requirements
* Python 3.5 or newer
    - to install please visit [https://www.python.org/](https://www.python.org/)
* Requests
    - If you have `pip` installed.
        - `pip install requests`
    - To install please visit: http://docs.python-requests.org/en/master/user/install/
   
# To Start
If you are on a Linux/Mac Machine
```python
python3 main.py
```

Otherwise executed main.py

# About
The directory has 4 main files.

## api.py
Handles the API Requests between the app and the server, this module depends on **Requests**

## main.py
Is the main app file, this python file is the core of the program.

## Utils.py
Is a set of Utilities that transacts the api requests using `api.py` and beautifies it into UI

## zendesk-api-unittest.py
Is the unittesting library which uses Python's built in library

# LICENSE
N/A
