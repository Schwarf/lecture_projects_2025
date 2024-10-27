
# BAD example
class UserManager:
    def __init__(self, user_data):
        self.user_data = user_data

    def save_to_database(self):
        # code to save user data
        pass

    def send_welcome_email(self):
        # code to send email
        pass



# GOOD EXAMPLE
class User:
    def __init__(self, user_data):
        self.user_data = user_data

class DatabaseManager:
    def save_user(self, user):
        # code to save user data
        pass

class EmailService:
    def send_welcome_email(self, user):
        # code to send email
        pass



#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
