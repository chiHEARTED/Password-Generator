import random



print('Welcome to the Password Generator!')

char = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z', '0','1','2','3','4','5','6','7','8','9','!','@','#','$','%','^','&','*','+','_','-','?']

length = int(input('How many characters would you like in your password?'))
password = ''
for c in range(length):
    password += random.choice(char)

print(password)

#To display password then closing program
input('Press enter to close program')
