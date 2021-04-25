import sqlite3

con = sqlite3.connect('user_info.db')

c = con.cursor()

def menu():
    menu_select = input("""Please Select an Option:
1: Input the info
2: Grab the Info
> """)
    if menu_select == '1':
        info_input()
    elif menu_select == '2':
        find_email()
    else:
        print("Did not give a valid option.")
        exit()


def info_input():
    name_input = input("Name: ")
    
    age_input = float(input("Age: "))
    
    org_input = input("School or Organization: ")
    
    address_input = input("Address: ")
    
    city_input = input("City: ")
    
    state_input = input("State: ")
    
    country_input = input("Country: ")
    
    email_input = input("Email for the account: ")

    pass_input = hash(input("Password for the account: "))

    c.execute(f"INSERT INTO test VALUES ('{email_input}', '{pass_input}')")

    con.commit()

    con.close()

def find_email():
    email_finder = input("Email that is attached to the account: ")

    c.execute(f"SELECT * FROM test WHERE email='{email_finder}'")

    print(c.fetchall())

    con.commit()

    con.close()

menu()
