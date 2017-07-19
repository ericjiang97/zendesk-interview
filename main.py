from api import ZendeskAPI
from Utils import Utils
from zendeskExceptions import ZendeskExceptions

ZendeskAPI = ZendeskAPI("https://lorderikir.zendesk.com") #url can be changed
Utils = Utils()
complete = False


print("Welcome to the Zendesk Ticket Viewer App")
print()
while not complete:
    if (ZendeskAPI.loggedIn == True):
        Utils.printMenu()
        mode = input("Enter mode: ")
        if (mode.lower() == "printall"):
            newArray = ZendeskAPI.handleTicket()["tickets"]
            Utils.printTickets(newArray)
        if (mode.lower() == "print"):
            try:
                ticketID = int(input("Enter number: "))
                Utils.printTickets([ZendeskAPI.handleTicket(ticketID)["ticket"]])
            except ValueError:
                print("Please enter a valid number. ")
            except ZendeskExceptions:
                print("Ticket not Found")
        elif (mode.lower() == "exit"):
            complete = True
    else:
        print()
        print("You are currently not logged in. Please enter your email and password to continue")
        email = input("Email: ")
        password = input("Password: ")
        try:
            ZendeskAPI.handleLogin(email, password)
        except ZendeskExceptions as e:
            print("Error: " + e)
