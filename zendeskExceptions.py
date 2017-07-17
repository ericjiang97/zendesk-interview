class ZendeskExceptions(Exception):
    def __init__(self, message):
        super(ZendeskExceptions, self).__init__(message)

    def __str__(self):
        return super(ZendeskExceptions, self).__str__()