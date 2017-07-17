import unittest
from api import ZendeskAPI
from zendeskExceptions import ZendeskExceptions
import json

class ABLTestModule(unittest.TestCase):
    def test_checkInitialise(self):
        self.assertTrue(ZendeskAPI().id == "", "Initalised Empty")

    def test_checkLogin(self):
        # make sure when it successfully logins it returns a name
        self.assertTrue(ZendeskAPI().handleLogin("ericjiang.work@gmail.com", "DF4huJ3OPDsv")["users"][0]["name"] == "Eric Jiang", "Ensures when it successfully logins it returns a name")
        # make sure it raises an exception when it fails
        with self.assertRaises(ZendeskExceptions):
            ZendeskAPI().handleLogin("stupid@email.fake.com", "definatelyarealpassword")

    def test_checkProfileLoading(self):
        z = ZendeskAPI()
        z.handleLogin("ericjiang.work@gmail.com", "DF4huJ3OPDsv")
        self.assertEqual(z.loggedIn, True, "Changed Logged in State to True")
        self.assertEqual(z.name, "Eric Jiang", "Changed Logged in State to True")

    def test_ticket(self):
        z = ZendeskAPI()
        z.handleLogin("ericjiang.work@gmail.com", "DF4huJ3OPDsv")
        expectedFile = open("./test_data/68.json")
        expectedFile = json.loads(expectedFile)
        print(expectedFile)
        z.handleTicket(z.handleTicket(68))
        self.ass
        # make sure it raises an exception when it doesn't find the ticket
        with self.assertRaises(ZendeskExceptions):
            z.handleTicket(40000213012301)



if __name__ == '__main__':
    unittest.main()
