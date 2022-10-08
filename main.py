from connection import connection
from prettytable import PrettyTable
def welcome():
    '''This function will start the program'''
    print("Welcome to Contacts")
    response = input("\t Select from the option below:\n \t [R]\t-Register\n \t [L]\t-Login\n")
    if response.upper() == "R":
        fName = input("\t Enter First Name:\t\t")
        lName = input("\t Enter Last Name:\t\t")
        email = input("\t Enter Email:\t\t\t")
        password = input("\t Enter Password:\t\t")
        cpassword = input("\t Enter Confirm Password:\t")
        phone = input("\t Enter Phone:\t\t\t")
        assert password == cpassword,"Password did not match"
        query = f'''INSERT INTO public."Users"(
        "FirstName", "LastName", "Email", "Password", "PhoneNumber")
        VALUES ('{fName}', '{lName}', '{email}', '{password}', {phone});commit;'''
        check_query = f'''SELECT "Email", "Password" FROM public."Users" where "Email" = '{email}' ;'''
        q = {"reg_query": query,"check_qery":check_query}
        status = connection(**q)
        print(status)
    

    elif response.upper() == "L":
        uid = input("\t Enter Email:\t\t")
        lpwd = input("\t Enter Password:\t")
        login_query = f'''SELECT "Password" FROM public."Users" where "Email" = '{uid}' ;'''
        q = {"login_query": login_query,"pwd":lpwd}
        res = connection(**q)
        if res == "Success":
            while True:
                print("What do you want to do?")
                print("="*50)
                selected_option = input('''
                [view -a]\t To view all the saved contact\n
                [view]\t To view specific contact\n
                [add]\t To add new contact\n
                [del]\t To delete a contact\n
                [del -a]\t To delete a contact\n
                [update]\t To update an existing contact\n
                [exit]\t To exit the program\n''')
        
                match selected_option.lower():
                    case "view -a":
                        pt = PrettyTable()
                        print("*"*20,"Your Contact List","*"*20)
                        all_query = f'''SELECT * FROM public."Users";'''
                        q = {"all_query": all_query}
                        res = connection(**q)
                        pt.field_names = [ "ContactID","FirstName", "LastName", "Email", "Password", "PhoneNumber"]
                        for record in res:
                            pt.add_row(list(record))
                        print(pt)
                        print("*"*20,"Your Contact List Ends","*"*20,"\n")
                    case "view":
                        pt = PrettyTable()
                        print("*"*20,"Selected Contact","*"*20)
                        uid = input("\t Enter Email:\t\t")
                        view_query = f'''SELECT * FROM public."Users" where "Email" = '{uid}' ;'''
                        q = {"view_query":view_query }
                        res = connection(**q)
                        pt.field_names = [ "ContactID","FirstName", "LastName", "Email", "Password", "PhoneNumber"]
                        for record in res:
                            pt.add_row(list(record))
                        print(pt)
                        print("*"*20,"End","*"*20,"\n")
                    case "add":
                        fName = input("\t Enter First Name:\t\t")
                        lName = input("\t Enter Last Name:\t\t")
                        email = input("\t Enter Email:\t\t\t")
                        password = input("\t Enter Password:\t\t")
                        cpassword = input("\t Enter Confirm Password:\t")
                        phone = input("\t Enter Phone:\t\t\t")
                        assert password == cpassword,"Password did not match"
                        query = f'''INSERT INTO public."Users"(
                        "FirstName", "LastName", "Email", "Password", "PhoneNumber")
                        VALUES ('{fName}', '{lName}', '{email}', '{password}', {phone});commit;'''
                        check_query = f'''SELECT "Email", "Password" FROM public."Users" where "Email" = '{email}' ;'''
                        q = {"reg_query": query,"check_qery":check_query}
                        status = connection(**q)
                        print(status)
                    case "del":
                        email = input("\t Enter Email to delete contact:\t\t\t")
                        del_query = f'''DELETE FROM public."Users" WHERE "Email" = '{email}';commit;'''
                        q={"del_query":del_query}
                        res = connection(**q)
                        print(res)
                    case "update":
                        colName = input("\t Enter column name to update from below: \n FirstName \tLastName \tPassword\n ")
                        upd_val = input("Enter the value to update the detail\t")
                        email = input("Entere email to update the details")
                        update_query = f'''UPDATE public."Users" SET "{colName}"='{upd_val}' WHERE "Email" = '{email}';commit;'''
                        q={"update_query":update_query}
                        res = connection(**q)
                        print(res)
                    case "del -a":
                        del_all_query = f'''TRUNCATE public."Users";commit;'''
                        q={"del_all_query":del_all_query}
                        res = connection(**q)
                        print(res)
                    case "exit":
                        print("Exited Successfully....")
                        break
        else:
            print(res)    

    else:
        print("Enter correct Options [R/L]")


if __name__ == "__main__":
    welcome()