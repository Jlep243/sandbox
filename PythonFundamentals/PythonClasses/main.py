class User: #Classes in python use PascalCase and snake_case used for everything else in python

    def __init__(self, user_id, username): #This function is called when a new object is made. This is called initialize function.
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1 #The self keyword is important in classes as it refers to objects made in classes
        self.following += 1


user_1 = User("001","Joey Salads")
user_2 = User("002", "Jack")

user_1.follow(user_2)
