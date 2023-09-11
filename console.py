from error_console import Error
import datetime

logo = """                                                
          / /                 //    ) ) //   ) ) 
         / / ( )  _   __     //    / / //___/ /  
        / / / / // ) )  ) ) //    / / / __  (    
       / / / / // / /  / / //    / / //    ) )   
 ((___/ / / / // / /  / / //____/ / //____/ /    

"""

print(logo)

db_filename = None

while True:
    cmd = input("[>] ").split(' ')

    if cmd[0] == "exit" or cmd[0] == "quit":
        quit()
    
    if cmd[0] == "set":
        err = Error(cmd="set")
        try:
            if cmd[1] == "db":
                db_filename = cmd[2]
                if ".jdb" in cmd[2]:
                    print(f"[+] Successfully set the database to {db_filename}")
                else:
                    err.spit_error(id=1)
    
        except Exception as e:
            err.spit_error(id=0)
        
    if cmd[0] == "add":
        print(f"         [+] Add Session - {datetime.datetime.now()}")
        print(" ")
        usr = input("   [username > ] ")
        email = input("   [email >] ")
        passwrd = input("   [password > ] ")
        id = 1
        print(" ")
        decision = input(f"[?] Confirm addition (y/n) > ")      
        
        if decision == "y":
            print(" ")
            print(f"""[+] Successfully added user
| 
| ID       : {id}
| Username : {usr}
| Email    : {email}
| Password : {passwrd}
|______________""")
            print(" ")
        
        else:
            print("[+] Cancelled addition")
            
               
    else:
        if cmd[0] == "":
            pass
        else:
            print(f'[!] Unrecognized command, type "help" for help')