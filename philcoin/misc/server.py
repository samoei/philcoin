import asyncio

class ConnectionPool:
    def __init__(self):
        self.connection_pool = set()

    def send_welcome_message(self, writer):
        """ Sends a welcome message to a newly connected client """
        pass

    def broadcast(self,writer, message):
        """ Broadcasts a general message to the entire pool """
        pass

    def broadcast_user_joins(self, writer):
        """ Calls the broadcast method with a "user joining" message"""
        pass

    def broadcast_user_quits(self, writer):
        """   Calls the broadcast method with a "user quitting" message """
        pass

    def broadcast_new_message(self, writer, message):
        """ Calls the broadcast method with a user's chat message """
        pass

    def list_users(self, writer):
        """Lists all the users in the pool"""
        pass

    def add_new_user_to_pool(self, writer):
        """Adds a new user to our existing pool"""
        self.connection_pool.add(writer)

    def remove_user_from_pool(self, writer):
        """ Remove an existing user from our pool """
        self.connection_pool.remove(writer)
