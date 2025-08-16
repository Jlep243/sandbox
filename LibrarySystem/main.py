logged_in = False

def sign_in(logged_in):
   if logged_in == True:
        print('welcome to your account!') 

while logged_in != True:
    login_or_register = input("Would you like to Login or Register: ")
    if login_or_register == "login":
        logged_in = True
        sign_in(logged_in)
    else:
        print('oops')
