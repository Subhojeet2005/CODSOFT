charcterslist=""
length=int(input("ENTER THE DESIRED LENGTH: "))
import string
import random
while True :
    print('Choose the specific add ons to your password: '+'\n'+'1. Digits'+'\n'+'2. Letters'+'\n'+'3. Special characters'+'\n'+'4. Exit')
    choice=int(input("Enter your choice: "))
    if choice==1:
        charcterslist=charcterslist+string.digits
    elif choice==2:
        charcterslist=charcterslist+string.ascii_letters
    elif choice==3:
        charcterslist=charcterslist+string.punctuation
    elif choice==4:
        print("THANK YOU FOR USING IT ")
        break 
password=[]
for i in range(length):
    fpassword=random.choice(charcterslist)
    password.append(fpassword)
print("The random password is : "+"".join(password))


