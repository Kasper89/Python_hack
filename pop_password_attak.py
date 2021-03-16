import requests

with open('pop_password.txt') as f:
    pop_passwords = f.read()

# print(pop_passwords[:100])
pop_passwords = pop_passwords.split('\n')
i=0


def bad_password_generator():
    global i
    password = pop_passwords[i]
    i += 1
    return password


login='admin'
susses=False
while not susses:
    password=bad_password_generator()
    data={'login':login,'password':password}

    response=requests.get('',json=data)

    if response.status_code==200:
        print(data)
        susses=True