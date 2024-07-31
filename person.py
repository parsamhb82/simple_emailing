import hashlib

class User:
    def __init__(self, username, password, initial_bool):
        self.username = username
        if initial_bool:
            self.password = self.hash_password(password)
        else:
            self.password = password
        self.emails = []

    def email_getter(self):
        return self.username

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password):
        return self.password == hashlib.sha256(password.encode()).hexdigest()

    def view_emails(self):
        counter = 0
        for email in self.emails:
            print(f'{counter} - {email[0]}')
            print(email[1])
            counter += 1

    def change_password(self, old_password, new_password):
        if self.check_password(old_password):
            self.password = self.hash_password(new_password)
            print("Password changed successfully.")
        else:
            print("The previous password is incorrect.")
    
    def receive_email(self, text, sender_email):
        self.emails.append([sender_email, text])


class AdminHandler(User):
    def __init__(self, username, password, initial_bool):
        super().__init__(username, password, initial_bool)
        self.users_list = []
        self.emails = []

    def add_user(self, username, password, initial_bool):
        new_user = User(username, password, initial_bool)
        self.users_list.append(new_user)

    def find_by_email(self, email):
        for user in self.users_list:
            if user.email_getter() == email:
                return user
        return None

    def send_email(self, text, sender_email, receiver_email, cc=[]):
        sender = self.find_by_email(sender_email)
        receiver = self.find_by_email(receiver_email)
        if receiver:
            receiver.receive_email(text, sender_email)
        for email in cc:
            cc_receiver = self.find_by_email(email)
            if cc_receiver:
                cc_receiver.receive_email(text, sender_email)