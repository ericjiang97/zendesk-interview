from api import ZendeskAPI
from Utils import Utils

ZendeskAPI = ZendeskAPI()
Utils = Utils()
complete = False

while not complete:
    if (ZendeskAPI.loggedIn == True):
        Utils.printMenu()
        mode = input("Enter mode: ")
        if (mode.lower() == "printall"):
            newArray = ZendeskAPI.handleTickets()["tickets"]
            Utils.printTickets(newArray)
        if (mode.lower() == "print"):
            try:
                ticketID = int(input("Enter number: "))
                Utils.printTickets([ZendeskAPI.handleTicket(ticketID)["ticket"]])

            except ValueError:
                print("Please enter a valid number. ")
        elif (mode.lower() == "exit"):
            complete = True
    else:
        print("Unfortunately You are Not Logged in. Please enter your email and password to continue")
        email = input("Email: ")
        password = input("Password: ")
        try:
            ZendeskAPI.handleLogin(email, password)
        except Exception:
            print("Invalid Email or Password.")