from time import time
import hashlib
import uuid
import pwinput
import psycopg2
import pyfiglet


sqluser = 'username'
sqlpass = 'password'
dbname = 'postgres'
host = 'localhost'
port = '5432'

con = psycopg2.connect(dbname=dbname, user=sqluser, password=sqlpass, host=host, port=port)

cursor = con.cursor()

# query = 'select * from user_info'

# df = pd.read_sql_query(query,con)


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

    sql = "select * from user_info"
    cursor.execute(sql)
    list = cursor.fetchall()
    for user in list:
        if user[1] == username:
            print(pyfiglet.figlet_format('Username already exist'))
            return

    sql = "INSERT INTO user_info(name,password,salt) VALUES ('{}','{}','{}')".format(username,newPassword,salt)
    cursor.execute(sql)
    con.commit()
    print(pyfiglet.figlet_format("register succees"))

def login(username,password):
    sql = "select * from user_info"
    cursor.execute(sql)
    list = cursor.fetchall()
    # user[1] = username
    # user[2] = passord
    # user[3] = salt
    for user in list:
        if user[1] == username:
            hashPassword = hashlib.sha256(user[3].encode() + password.encode()).hexdigest()
            if hashPassword == user[2]:
                print(pyfiglet.figlet_format("Login success"))
            else:
                print(pyfiglet.figlet_format("Wrong Username & Password"))
def main():
    print(pyfiglet.figlet_format("Register System"))
    option = -1
    while option != 0:
        print(f"1. Register\n2. Login\n0.Exit")
        option = int(input("Please input an options: "))
        if option == 0:
            print("exiting the program")
            break
        elif option == 1:
            u = input("Please enter username: ")
            p = pwinput.pwinput(prompt="Please input password ", mask='*')
            RegisAccount(u, p)
        elif option == 2:
            print("Login Pages")
            username = input("Enter your username: ")
            if username != "":#change this
                print("checking username")
                print("username is right")
                password = pwinput.pwinput(prompt="type your password: ", mask='*')
                if password != "":#change this
                    login(username, password)
                else:
                    exit()
            else:
                exit()    
if __name__ == "__main__":
    main()