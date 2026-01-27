import os, getpass, fun, hashlib, os
from time import sleep


account = {}
id = 1001 

                            
def clear_ter():                                        #function to clear terminal 
    os.system("cls" if os.name == "nt" else "clear")


while True:
    clear_ter()
    print("Select your choice from below options ")
    choice = input("1· Create an Account\n2. Manage Account\n(1/2/3) :  ")
     
    #  1 . account creation
    if choice == '1':
        result = fun.detail_intake()
        sleep(1)

        
        while True:
            clear_ter()
            false_pin = getpass.getpass("\nCreate pin : ")
            pin = getpass.getpass("Re-enter PIN : ") 
            if false_pin == pin:
                break
            else:
                print("\n Wrong PIN")
        
        sleep(1)
        

        while True:
            print(f"check your details carefully\n{result[0], result[1]}\n")
            retake = input(
                "- for resubmission press ENTER\n"
                "- To continue press enter any KEY\n"
            )
         

            if retake == '':
                clear_ter()
                result = fun.detail_intake()
                clear_ter()

                while True:
                  
                  false_pin = getpass.getpass("\nCreate pin : ")
                  pin = getpass.getpass("Re-enter PIN : ") 
                  if false_pin == pin:
                    break
                  else:
                    print("\n Wrong PIN")
                sleep(1)

            else:
                clear_ter()
                break

        sleep(1)
        print("Account is created successfuly")
        print(f"Your customer id is {id}\n")
        sleep(0.5)

        # 1.1 . pin hashing
        salt = os.urandom(12)
        hashed_pin = hashlib.sha256(salt + pin.encode()).hexdigest()


        account.update({str(id): {"name": result[0], "age": result[1], "h.pin" : hashed_pin, "salt" : salt}})
        id += 1



      # Manage account
    elif choice == '2':
        cust_id = input("Enter your customer ID : ")
        pin_in = getpass.getpass("Enter your PIN : ")

        def de_hashing():
            if hashlib.sha256(account[cust_id]["salt"] + pin_in.encode()).hexdigest() ==  account[cust_id]["h.pin"]:
             return True
            else:
             return False
        de_hash = de_hashing() 

        clear_ter()
        print("You Loged In**")
        sleep(1.5)
        clear_ter()

        
        if de_hash == True:
           while True:
              print("1.Cheack balance")
              print("2.Change pin")
              print("3.Exit")

              sub_choice = input("\nselect to option : ")
            


        
                
               

                   

            
                