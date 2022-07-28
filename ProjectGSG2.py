
from ProjectGSG1 import*

class Ticket:

    def ticket_show(self):
        bln = []
        with open("passenger_Data.csv",'r+',newline="") as f:
            r =  csv.reader(f)
            data = list(r)
            id = int(input("Enter Your Booking Id  :"))
            for i in data:
                if id == int(i[0]):
                    for j in i:
                        bln.append(j)
                    break

        print("------------------------------------------------------------------------------")
        print("                          Shloun Bus Travel                               ")
        print("------------------------------------------------------------------------------")
        print()
        print()
        print("",bln[3],"------------->",bln[4],"            ","        Passenger Id:",bln[0])
        print()
        print(" Passenger Name :", bln[1],"              ","Number of Passenger :",bln[2])
        print("______________________________________________________________________________")
        print()
        print(" Date of Booking :",bln[5],"              ","Seat No :",bln[6],"              ")
        print()
        print(" Bus Type :       ",bln[7],"                                                           ")
        print(" Bus Fare :       ",bln[8],"                                                           ")
        print()
        print("------------------------------------------------------------------------------")