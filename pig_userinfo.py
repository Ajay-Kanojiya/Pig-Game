
import csv
from pig_class_HC import Human_Computer



class Registration:

    def register(self):

        username = input('Enter the user name:').lower()
        password = str(input('Enter the password:'))
        confirm_password = str(input('Confirm password:'))

        if password == confirm_password:
            # password = password
            print('Congratulations! you have successfully registered. ')
        else:
            print('password and confirm password is not matching')

        with open('user_data.csv', 'a+', newline='') as file:
            write = csv.writer(file)
            # write.writerow(['user_name','password'])
            write.writerow([username, password])

    def login(self):
        while True:
            user_name = input('Please enter the user name:')
            password = input("Please enter the password:")
            # input('press enter to log in to your account')
            with open('user_data.csv', 'r') as file_read:
                read = csv.reader(file_read)
                if [user_name, password] in read:
                    print('logged in')
                    break
                else:
                    print('invalid username or password')

    def loginpage(self):
        print('--------------------------------Welcome to PIG Game-----------------------------------')
        print("---- Login -----or-------register")
        choose = input('press 1 for login and 2 for registration:')
        if '1' == choose:
            log = Registration()
            log.login()
            choose1 = input('press 1 for Quick match and  2 for Multiplayer')
            if choose1 == '1':
                hc = Human_Computer()
                hc.human_player()
            elif choose1 == '2':
                obj = H
                hh.player_one()
                hh.player_two(obj)

        else:
            log = Registration()
            log.register()
            log.login()


obj = Registration()
obj.loginpage()

