class Utils:
    def __init__(self):
        pass

    # Print Table Function
    def printTickets(self, array):
        for i in range(0, len(array), 25):
            maxEnd = i + 25
            currentArray = array[i:maxEnd]
            headerString = "ID  | " + "Type" + 8 * " " + " | " + "Subject" + 21 * " " + " | "
            print(headerString)
            print(len(headerString)*"-")
            for j in range(len(currentArray)):
                currentItem = currentArray[j]
                stringRow = str(currentItem["id"]) + (3 - len(str(currentItem["id"]))) * ' ' + " | "
                stringRow += str(currentItem["type"]) + (12 - len(str(currentItem["type"]))) * ' ' + " | "
                if (len(str(currentItem["subject"])) >= 25):
                    stringRow += str(currentItem["subject"][:25]) + "... | "
                else:
                    stringRow += str(currentItem["subject"]) + (25 - len(str(currentItem["subject"]))) * ' ' + "... | "
                print(stringRow)
            input("Press Enter to continue...")

    def printMenu(self):
        print()
        print("Zendesk Ticket Viewer")
        print()
        print("1. Type Printall to View All Available Tickets")
        print("2. Type Print to Print a Certain Tickets")
        print("3. Type Exit to Exit")
