import random
length = input(print('Enter the length of password you want: \n'))
chars = 'abcdefghijklmnopqrstuvwxyz$@-_.,?0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
password = ''
for i in range(length):
    password = password.write(random.choice(chars))

print("\n" + password)