from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key



def add():
    name = input('Account name: ')
    pwd = input('Password: ')
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + '\n')
    return

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            # print(line.rstrip())
            data = line.rstrip()
            user, password = data.split("|")
            print(user, fer.decrypt(password.encode()).decode())
            # print(line)
    return

#-------------------------#

master_pwd = input("What is the master password? ")
write_key()

key = load_key() + master_pwd.encode()
# key = load_key() 
fer = Fernet(key)   
print("fer: ", fer)


while True:
    
    mode = input("Would you like to add a new password or view an existing one (add or view)? Press Q to quit ").lower()
    
    if mode == 'q':
        break
    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('Invalid mode!')