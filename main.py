from ticketbooking import ticketinfo
# from <module-name> import <class-name>
class Main:
    def execute(self,choice):
        if choice == 1:
            print("*******Show the seats*******")
            movie_ticket_obj.show_seats()
        if choice == 2:
            print("*******Buy Ticket*******")
            movie_ticket_obj.buy_ticket()
        if choice == 3:
            print("*******statistics*******")
            movie_ticket_obj.statistics()
        if choice == 4:
            print("*******User Detail*******")
            movie_ticket_obj.user_info()
        if choice == 0:
            pass
            

if __name__ == "__main__":
    rows = int(input("Enter the number for rows : "))
    columns = int(input("Enter the number of seats in each rows : "))

    movie_ticket_obj = ticketinfo(rows,columns)
    obj = Main()

    while True:
        choice = int(input("Enter \n1.Show the seats \n2.Buy a ticket \n3.Statistics \n4.Show booked ticket's user info \n0.Exit : \n"))    
        obj.execute(choice)