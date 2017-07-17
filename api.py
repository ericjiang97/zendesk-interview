import requests
from Utils import Utils
from zendeskExceptions import ZendeskExceptions

class ZendeskAPI:
    def __init__(self):
        self.name = ""
        self.id = ""
        self.email = ""
        self.password =""
        self.loggedIn = False
        pass

    def handleLogin(self, user, password):
        r = requests.get('https://lorderikir.zendesk.com/api/v2/users.json', auth=(user, password))
        if(r.status_code != 200):
            # reject login
            raise ZendeskExceptions('Unauthorised Login')
        else:
            user = r.json()
            self.id = user["users"][0]["id"]
            self.name = user["users"][0]["name"]
            self.email = user["users"][0]["email"]
            self.password = password
            self.loggedIn = True
            return user

    def handleTickets(self):
        # /api/v2/tickets.json
        r = requests.get('https://lorderikir.zendesk.com/api/v2/tickets.json?per_page=500', auth=(self.email, self.password))
        if(r.status_code == 200):
            return r.json()
        elif(r.status_code == 500):
            return {"Unknown (Server) error occured. "}


    def handleTicket(self, id):
        # /api/v2/tickets.json
        r = requests.get('https://lorderikir.zendesk.com/api/v2/tickets/' + str(id) + '.json', auth=(self.email, self.password))
        if(r.status_code == 200):
            return r.json()
        elif(r.status_code == 404):
            raise ZendeskExceptions('Ticket Not Found')
        elif(r.status_code == 500):
            return {"Unknown (Server) error occured. "}



