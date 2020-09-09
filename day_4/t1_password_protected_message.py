password = 'cupcakes'
guess = ''
secret_message = 'Tomorrow, I will bring cookies for me and you to share at lunch!'

print(f'Please enter the correct password:')
guess = input()

while guess != password: 
    print(f'Wrong!')
    print(f'Please enter the correct password:')
    guess = input()

print(f"Correct password! The secret message is {secret_message}") 
