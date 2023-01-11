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
                    if self.booked_ticket(i,j):
                        print("B",end=" ")
                    else:
                        print("S",end=" ")
            print()

            
    def buy_ticket(self):
        buy_row=int(input("Enter the row number : "))
        buy_col=int(input("Enter the col number : "))
        
        total_seats = self.rows * self.cols

        if  total_seats <= 60:
            ticket_price=10
        else:
             if (self.rows//2)<=buy_row:
                 ticket_price=8
             else:
                 ticket_price=10
                 

        ch=int(input(f"You have choose row {buy_row} and col {buy_col}. the Price of this ticket is {ticket_price}\nAre you Sure You want to continue 1.Yes. 2. No  :  "))
        if ch==1:
            name = input("Enter Your Name : ")
            Gender = input("Enter Your Gender : ")
            Age = int(input("Enter Your Age : "))
            phone_no = input("Enter Your Mobile No : ")
            TicketId = str(buy_row)+str(buy_col)
            self.user_detail[TicketId]=[name,Gender,Age,phone_no,ticket_price]
            print("Ticket booked Successfully..........")
            print(self.user_detail)
        else:
            print("User Aborted Ticket booking. No ticket booked...")

    def statistics(self):
        no_of_ticket_booked=len(self.user_detail)
        total_seats = self.rows * self.cols
        percentage_booked_seats= (no_of_ticket_booked/total_seats)*100

        all_ticket_price=[]
        for k,v in self.user_detail.items():
            all_ticket_price.append(v[4])
        current_income=sum(all_ticket_price)

        if  total_seats <= 60:
            total_income = total_seats * 10
        else:
            front_price = 10
            back_price = 8
            front_seats = (self.rows//2)*self.cols
            total_income = front_seats * front_price + (total_seats - front_seats) * back_price
#                              
        print("Number of Purchased Tickets : ",no_of_ticket_booked)
        print(f"Percentage : {percentage_booked_seats}%")
        print(f"Current income: ${current_income}")
        print(f"Total income : ${total_income}")
    
    def user_info(self):
        row1=int(input("Enter the row number : "))
        col1=int(input("Enter the col number : "))
        seatId=str(row1)+str(col1)
        userdetail=self.user_detail.get(seatId,None)

        if userdetail:
            print('''Name           :       ''',userdetail[0])
            print('''Gender         :       ''',userdetail[1])
            print('''Age            :       ''',userdetail[2])
            print('''Ticket Price   :       ''',userdetail[3])
            print('''Phone Number   :       ''',userdetail[4])
        else:
            print(f"No Such Ticket booked W.R.F Row Number {row1} and Column Number{col1}.")
        
    def booked_ticket(self,row,col):
        ticketid=str(row)+str(col)
        for k,v in self.user_detail.items():
            if ticketid==k:
                return True
            
            

