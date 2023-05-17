from cryptography.fernet import Fernet

def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key

'''
def write_key():
    key = Fernet.generate_key()
    with open('key.key', "wb") as key_file:
        key_file.write(key)'''

# write_key()

# master_pwd = input('Enter the master password: ')
# with open('password.txt', 'a')
key = load_key() #+ master_pwd.encode()
fer = Fernet(key)


def view():
    with open('password.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            acc,pwd = data.split('|')
            print('Account Name :', acc , 'Password :', fer.decrypt(pwd.encode()).decode())

def add():
    name = input('Account name: ')
    pwd = input('Password: ')

    with open('password.txt','a') as f:
        f.write(name + '|' + fer.encrypt(pwd.encode()).decode() + '\n')


while True:
    mode = input('Would you like to add a new password or view the existing ones? (add/view) , to quit enter (q)')
    if mode == 'q':
        break

    if mode == 'add':
        add()
    elif mode == 'view':
        view()
    else:
        print('Invalid input')
        continue