import random
caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud = int(input('Intruduce la longitud de la contraseña:'))
contraseña = ''
for i in range(longitud):
    contraseña += random.choice(caracteres)
print(f'Tu contraseña de longitud {longitud} es: {contraseña}')
