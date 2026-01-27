def detail_intake():                                    #function for inputing user details
    while True:
        try:
            name = input("Enter your Full name : ")
            age = int(input("Enter your age : "))
            if age < 18:
                print("\nYou are not eligable yet. ")
            else:
                break

        except ValueError:  
            print("·(age should only contain integeres)")
       
    return name, age
        
             
def de_hashing():
    if hashlib.sha256(account[cust_id]["salt"] + pin_in.encode()).hexdigest() ==  account[cust_id]["hashed_pin"]:
         return True
    else:
        return False




   
   

