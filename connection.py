from cgi import print_arguments
from itertools import count
from postgres import psycopg2 as pg
def connection(**kwrgs):
    '''Will create the connection object'''    
    connection = pg.connect("dbname=Users user=postgres password=root")
    cursor = connection.cursor()
    key = [i for i in kwrgs.keys()]
    if "check_qery" in key:
        cursor.execute(kwrgs.get("check_qery"))
        login_data = cursor.fetchone()
        if login_data is None:

            if key[0] == "reg_query":
                # print(kwrgs.get("reg_query"))
                insert_res = ""
                try:
                    insert_res = cursor.execute(kwrgs.get("reg_query"))
                except Exception as e:
                    pass
                finally:
                    connection.close()
                return "Successfully registered..."
        else:
            connection.close()
            return "Email Id already registered.."


    if  "login_query" in key:
        cursor.execute(kwrgs.get("login_query"))
        login_data = cursor.fetchone()  
        if login_data is not None:
            for j in login_data:
                if kwrgs.get("pwd") == j:
                    print("\t Login successfull!!!")
                    return "Success"
                else:
                    return "Incorrect password"
        else:
            return "Please register before login.."

    if "all_query" in key:
        cursor.execute(kwrgs.get("all_query"))
        login_data = cursor.fetchall()  
        connection.close()
        return login_data

    if "view_query" in key:
        cursor.execute(kwrgs.get("view_query"))
        specific_record = cursor.fetchall()  
        connection.close()
        return specific_record

    if "del_query" in key:
        del_res = cursor.execute(kwrgs.get("del_query")) 
        connection.close() 
        return del_res
    
    if "update_query" in key:
        upd_res = cursor.execute(kwrgs.get("update_query")) 
        connection.close() 
        return upd_res
    
    if "del_all_query" in key:
        upd_res = cursor.execute(kwrgs.get("del_all_query"))  
        connection.close()
        return upd_res

    return cursor