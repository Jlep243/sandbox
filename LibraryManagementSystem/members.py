class Members:

    def __init__(self,username, password):
        self.user = username
        self.password = password
        

    def __str__(self):
        return self.user
