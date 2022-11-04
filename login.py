class LoginNotLettersException(Exception):
    pass

class PassNotNumbersException(Exception):
    pass

def input_login():
    try:
        login=input("Please enter a login ")
        if login.isalpha()==False or login.islower()==False:
            raise LoginNotLettersException("Login must contain lower letters only")

    
    except LoginNotLettersException as lnl: 
         print(lnl)
         return False

    else:
        return True
    

def input_password():
    try:
        passwrd=input("Please enter a login ")
        if passwrd.isnumeric()==False:
            raise PassNotNumbersException("Password must contain numbers only")
    except PassNotNumbersException as pnn: 
         print(pnn)
         return False
    else:
        return True


if __name__ == '__main__':
    login = False
    passwrd=False

    while login == False:
        try:
            login = input_login()
        
        except LoginNotLettersException as lnl: 
            print(lnl)
        if login!=False:
            break

      
    
          
    
    

        
            
        
        

    
    
        













