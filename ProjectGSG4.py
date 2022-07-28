from ProjectGSG1 import *
from ProjectGSG2 import *
from ProjectGSG3 import *

global ch  # declared global variable

print("---------------------------------------------------")
print("           Welcome To Shloun  Bus Travel        ")
print("---------------------------------------------------")
print()


def start() -> object:
    print("1. Admin Registration :")
    print("2. Admin Login        :")
    print()
    admin_obj = Admin()
    ch = int(input("Choose Correct option :"))

    if ch == 1:
        # admin class object creation
        admin_obj.admin_registration()

    if ch == 2:

        admin_obj.admin_login()

        print()
        print("1. Passenger Registration :")
        print("2. Show Ticket            :")
        print()
        ch = int(input("Choose Any One Option :"))
        if ch == 1:
            pd_obj = Passenger_Data_Csv()
            pd_obj.get_Passenger_Info()
            pd_obj.save_info()
        elif ch == 2:
            obj = Ticket()
            obj.ticket_show()


start()
