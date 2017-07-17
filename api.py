import requests
from zendeskExceptions import ZendeskExceptions

'''
ZendeskAPI Class
:author: 
'''
class ZendeskAPI:
    def __init__(self, baseURL):
        if not baseURL:
            raise ZendeskExceptions("Base Zendesk URL Not Specified")
        # configuration
        self.baseURL = "https://lorderikir.zendesk.com"
        # user profile
        self.name = ""
        self.id = ""
        self.email = ""
        self.password =""
        self.loggedIn = False
        pass

    def handleLogin(self, user, password):
        '''
        Handles the Login Via the API (ensures the user can login)
        :param user: the username
        :param password: the password
        :return: user profile
        :raises: ZendeskExceptions when the user is not authenticated
        '''
        r = requests.get(self.baseURL + '/api/v2/users.json', auth=(user, password))
        print(r.status_code)
        if(r.status_code == 200):
            user = r.json()
            self.id = user["users"][0]["id"]
            self.name = user["users"][0]["name"]
            self.email = user["users"][0]["email"]
            self.password = password
            self.loggedIn = True
            return user
        elif(r.status_code == 500):
            # reject login
            raise ZendeskExceptions('Service is currently unavialable. Please try again later.')
        else:
            # reject login
            raise ZendeskExceptions('Unauthorised Login')

    def handleTicket(self, id):
        '''
        Grabs Ticket(s) via the Zendesk API
        :param id:  the ticket id you want to load, otherwise all when null
        :return: when null: returns all the tickets, otherwises returns a certain ticket using the ticket id
        :raises: ZemdeskExceptions when the ticket can not be found, when the user is unauthourised or when the service is unavialable
        '''
        if(id):
        # /api/v2/tickets/:id.json
            r = requests.get(self.baseURL + '/api/v2/tickets/' + str(id) + '.json',
                             auth=(self.email, self.password))
            if (r.status_code == 200):
                return r.json()
            elif (r.status_code == 404):
                raise ZendeskExceptions('Ticket Not Found')
            elif (r.status_code == 500):
                return {"Unknown (Server) error occured. "}
        else:
        # /api/v2/tickets.json
            r = requests.get(self.baseURL + '/api/v2/tickets.json?per_page=500', auth=(self.email, self.password))
            if(r.status_code == 200):
                return r.json()
            elif(r.status_code == 500):
                return {"Unknown (Server) error occured. "}



