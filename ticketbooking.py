class ticketinfo:
    def __init__(self, rows, cols):
      self.rows=rows
      self.cols=cols
      self.user_detail={}
      
    def show_seats(self):
        for i in range(self.rows+1):
            for j in range(self.cols+1):
                if i==0:
                    if j==0:
                        print(" ",end=" ")
                    else:
                        print(j,end=" ")
                elif j==0:
                    print(i,end=" ")
                else:
                    print("S",end=" ")
            print()

            
    def buy_ticket(self):
        buy_row=int(input("Enter the row number : "))
        buy_col=int(input("Enter the col number : "))
        ticket_price=10
        ch=int(input(f"You have choose row {buy_row} and col {buy_col}. the Price of this ticket is {ticket_price}\nAre you Sure You want to continue 1.Yes. 2. No  :  "))
        if ch==1:
            name = input("Enter Your Name : ")
            Gender = input("Enter Your Gender : ")
            Age = int(input("Enter Your Age : "))
            phone_no = input("Enter Your Mobile No : ")
            TicketId = str(buy_row)+str(buy_col)
            self.user_detail[TicketId]=[name,Gender,Age,phone_no]
            print("Ticket booked Successfully..........")
            print(self.user_detail)
        else:
            print("User Aborted Ticket booking. No ticket booked...")






