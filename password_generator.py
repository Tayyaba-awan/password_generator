#create a password generator
import random
letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
        'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbol=['!','@','#','$','%','^','&','*','(',')']
number=['1','2','3','4','5','6','7','8','9','0']
list=['letter','symbol','number']
random.shuffle(list)
print("welcome to the pypassword genertor")
letter_pass=int(input("how many letter would you like in you password"))
symbol_pass=int(input("how many symbol would you like"))
number_pass=int(input("how many number would you like"))
password_list=[]
for n in range(1,letter_pass+1):
   #char=random.choice(letter)
   #password+=char
   password_list+=random.choice(letter)
for n in range(1,symbol_pass+1):
   password_list+=random.choice(symbol)
for n in range(1,number_pass+1):
   password_list+=random.choice(number)
random.shuffle(password_list)
password=""
for n in password_list:
     password+=n
print(f"here is your password {password}")