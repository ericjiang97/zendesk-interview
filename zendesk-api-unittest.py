import unittest
from api import ZendeskAPI
from zendeskExceptions import ZendeskExceptions
import json

class ABLTestModule(unittest.TestCase):
    def test_checkInitialise(self):
        self.assertTrue(ZendeskAPI("https://lorderikir.zendesk.com").id == "", "Initalised Empty")
        # ensure it raises an error when no baseURL is declared
        with self.assertRaises(ZendeskExceptions):
            ZendeskAPI("")

    def test_checkLogin(self):
        # make sure when it successfully logins it returns a name
        self.assertTrue(ZendeskAPI("https://lorderikir.zendesk.com").handleLogin("ericjiang.work@gmail.com", "DF4huJ3OPDsv")["users"][0]["name"] == "Eric Jiang", "Ensures when it successfully logins it returns a name")
        # make sure it raises an exception when it fails
        with self.assertRaises(ZendeskExceptions):
            ZendeskAPI("https://lorderikir.zendesk.com").handleLogin("stupid@email.fake.com", "definatelyarealpassword")

    def test_checkProfileLoading(self):
        z = ZendeskAPI("https://lorderikir.zendesk.com")
        z.handleLogin("ericjiang.work@gmail.com", "DF4huJ3OPDsv")
        self.assertEqual(z.loggedIn, True, "Changed Logged in State to True")
        self.assertEqual(z.name, "Eric Jiang", "Changed Logged in State to True")

    def test_ticket(self):
        z = ZendeskAPI("https://lorderikir.zendesk.com")
        z.handleLogin("ericjiang.work@gmail.com", "DF4huJ3OPDsv")
        with open('./test_data/68.json') as data_file:
            data = json.load(data_file)
        actualResponse = z.handleTicket(68)
        self.assertEqual(data, actualResponse, "Ensure that the ticket data matches")

        # make sure it raises an exception when it doesn't find the ticket

        with self.assertRaises(ZendeskExceptions):
            z.handleTicket(40000213012301)



if __name__ == '__main__':
    unittest.main()
