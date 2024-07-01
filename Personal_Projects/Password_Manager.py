from cryptography.fernet import Fernet

'''def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            if data:
                wuser, uuser, passw = data.split(" | ")
                wuser = wuser.replace("Account Name: ", "")
                uuser = uuser.replace("Username: ", "")
                passw = passw.replace("Password: ", "")
                print(f"Website: {wuser}, Username: {uuser}, Password: {fer.decrypt(passw.encode()).decode()}")

def add():
    website = input('Website: ')
    username = input('Username: ')
    password = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(f"Account Name: {website} | Username: {username} | Password: {fer.encrypt(password.encode()).decode()}\n")

while True:
    mode = input("Would you like to 'add' a new password, 'view' a file, or quit using 'q'? ").lower()
    if mode == 'q':
        break
    elif mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('Invalid input')
