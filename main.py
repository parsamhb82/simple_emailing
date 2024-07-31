from person import User, AdminHandler
import json

with open('users.json', 'r') as file:
    users_list = json.load(file)
admin = AdminHandler(users_list[0][0], users_list[0][1], False)
admin.emails = users_list[0][2]

for user in users_list:
    admin.add_user(user[0], user[1], False)
    this_user = admin.find_by_email(user[0])
    this_user.emails = user[2]

print('Welcome')
while True:
    email = input('Enter your email (enter 0 for exit): ')
    if email == '0':
        emails_passwords = [[user.email_getter(), user.password, user.emails] for user in admin.users_list]

        with open('users.json', 'w') as json_file:
            json.dump(emails_passwords, json_file, indent=4)

        with open('emails.json', 'w') as json_file:
            json.dump(admin.emails, json_file, indent=4)

        exit()
    password = input('Enter your password: ')
    if email == admin.email_getter() and admin.check_password(password):
        print('Welcome admin')
        while True:
            inp = input('What do you want to do\n1 - Send email\n2 - See your emails\n3 - Change password\n4 - Sign out\n5 - Add new user\n')
            if inp == '1':
                receiver_email = input('Receiver email: ')
                text = input('Text: ')
                while True:
                    cc_ = input('Do you want to have cc? 1 - Yes 2 - No ')
                    if cc_ == '2':
                        admin.send_email(text, admin.email_getter(), receiver_email)
                        break
                    elif cc_ == '1':
                        cc = []
                        while True:
                            cc_username = input('Enter the username (0 for exit this part): ')
                            if cc_username == '0':
                                break
                            cc.append(cc_username)
                        admin.send_email(text, admin.email_getter(), receiver_email, cc)
                        break
                    else:
                        print('Wrong')
            elif inp == '2':
                admin.view_emails()
                reply_to = input('Do you want to reply? 1 - Yes 2 - No ')
                if reply_to == '1':
                    while True:
                        index = int(input('Enter the number of email: '))
                        if 0 <= index < len(admin.emails):
                            break
                        else:
                            print('Index not true')
                    text = input('Enter the text: ')
                    admin.send_email(text, admin.email_getter(), admin.emails[index][0])
            elif inp == '3':
                old_password = input('Enter your old password: ')
                new_password = input('Enter new password: ')
                admin.change_password(old_password, new_password)
            elif inp == '4':
                break
            elif inp == '5':
                email = input('Enter the email: ')
                password = input('Enter your password: ')
                admin.add_user(email, password, True)
    else:
        user = admin.find_by_email(email)
        if user and user.check_password(password):
            print('Welcome user')
            while True:
                inp = input('What do you want to do\n1 - Send email\n2 - See your emails\n3 - Change password\n4 - Sign out\n')
                if inp == '1':
                    receiver_email = input('Receiver email: ')
                    text = input('Text: ')
                    while True:
                        cc_ = input('Do you want to have cc? 1 - Yes 2 - No ')
                        if cc_ == '2':
                            admin.send_email(text, user.email_getter(), receiver_email)
                            break
                        elif cc_ == '1':
                            cc = []
                            while True:
                                cc_username = input('Enter the username (0 for exit this part): ')
                                if cc_username == '0':
                                    break
                                cc.append(cc_username)
                            admin.send_email(text, user.email_getter(), receiver_email, cc)
                            break
                        else:
                            print('Wrong')
                elif inp == '2':
                    user.view_emails()
                    reply_to = input('Do you want to reply? 1 - Yes 2 - No ')
                    if reply_to == '1':
                        while True:
                            index = int(input('Enter the number of email: '))
                            if 0 <= index < len(admin.emails):
                                break
                            else:
                                print('Index not true')
                        text = input('Enter the text: ')
                        admin.send_email(text, user.email_getter(), user.emails[index][0])

                elif inp == '3':
                    old_password = input('Enter your old password: ')
                    new_password = input('Enter new password: ')
                    user.change_password(old_password, new_password)
                elif inp == '4':
                    break