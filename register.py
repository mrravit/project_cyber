from time import time
import hashlib
import uuid


list = []


class User:
    def __init__(self, name , password,salt):
        self.name = name
        self.password = password
        self.salt = salt


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected Character")
        self._name = value


def RegisAccount(username, password):
    username = username
    password = str(password)
    salt = uuid.uuid4().hex
    newPassword = hashlib.sha256(salt.encode() + password.encode()).hexdigest()

    list.append(User(username, newPassword, salt))

def login(username,password):
    for user in list:
        if user.name == username:
            hashPassword = hashlib.sha256(user.salt.encode() + password.encode()).hexdigest()
            if hashPassword == user.password:
                print("Login success")
            else:
                print("Wrong Username & Password")
def main():
    print("Test project cyber")
    option = -1
    while option != 0:
        print(f"1. Register\n2. Login\n 0.Exit")
        option = int(input("Please input an options: "))
        if option == 0:
            print("exiting the program")
            break
        elif option == 1:
            u = input("Please enter username: ")
            p = input("Please input password ")
            RegisAccount(u, p)
        elif option == 2:
            print("Login Pages")
            username = input("Enter your username: ")
            if username != "":#change this
                print("checking username")
                print("username is right")
                password = input("type your password: ")
                if password != "":#change this
                    login(username, password)
                else:
                    exit()
            else:
                exit()    
if __name__ == "__main__":
    main()