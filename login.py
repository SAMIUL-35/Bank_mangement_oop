users_login = {}  

class Login:
    loan = True
    isBankrupt=False
    
    def __init__(self, user_name, passd):
        self.user_name = user_name
        self.passd = passd

    @classmethod
    def is_user_registered(cls, name):
        return name in users_login