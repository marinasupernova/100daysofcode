pet_parade_order = [
    'Pete the Pug', 
    'Sally the Siamese Cat', 
    'Beau the Boxer', 
    'Lulu the Labrador', 
    'Lily the Lynx', 
    'Pauline the Parrot', 
    'Gina the Gerbil', 
    'Tubby the Tabby Cat']
del pet_parade_order[6]
print(f'{pet_parade_order}')
del pet_parade_order[5]
pet_parade_order [0:0] = ['Pauline the Parrot']
print(f'{pet_parade_order}')
pet_parade_order [6:6] = ['Mimi the Maltese Cat', 'Cory the Corgi']
print(f'{pet_parade_order}')
del pet_parade_order[4:6]
print(f'{pet_parade_order}')